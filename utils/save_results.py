#!/usr/bin/env python3
"""
Save Generated Results Utility

Utility to organize and save all matplotlib test results with proper naming
and timestamping for better organization and tracking.
"""

import os
import shutil
from datetime import datetime
import glob


class ResultSaver:
    """Utility class to organize and save test results"""
    
    def __init__(self, base_dir: str = "test_results"):
        self.base_dir = base_dir
        self.ensure_directory_exists()
    
    def ensure_directory_exists(self):
        """Create base directory if it doesn't exist"""
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
    
    def get_timestamp(self) -> str:
        """Get current timestamp for unique naming"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def save_current_results(self, session_name: str = None) -> str:
        """
        Save current generated results with timestamped subdirectory
        
        Args:
            session_name: Optional name for the test session
            
        Returns:
            str: Path to the saved results directory
        """
        timestamp = self.get_timestamp()
        if session_name:
            session_dir = f"{session_name}_{timestamp}"
        else:
            session_dir = f"matplotlib_test_{timestamp}"
        
        save_path = os.path.join(self.base_dir, session_dir)
        os.makedirs(save_path, exist_ok=True)
        
        # Find all generated files in the base test_results directory
        files_to_save = []
        for pattern in ["*.png", "*.md", "*.pdf", "*.txt"]:
            files_to_save.extend(glob.glob(os.path.join(self.base_dir, pattern)))
        
        # Copy files to the timestamped directory
        saved_files = []
        for file_path in files_to_save:
            if os.path.isfile(file_path) and not os.path.basename(file_path).startswith(session_dir):
                dest_path = os.path.join(save_path, os.path.basename(file_path))
                shutil.copy2(file_path, dest_path)
                saved_files.append(dest_path)
                print(f"Saved: {dest_path}")
        
        # Create a summary file
        summary_path = os.path.join(save_path, "session_summary.txt")
        with open(summary_path, 'w') as f:
            f.write(f"Matplotlib Test Session Summary\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Session Name: {session_name or 'Default'}\n")
            f.write(f"Files Generated: {len(saved_files)}\n\n")
            f.write("Generated Files:\n")
            for file_path in saved_files:
                f.write(f"- {os.path.basename(file_path)}\n")
        
        print(f"\nSession saved to: {save_path}")
        print(f"Total files saved: {len(saved_files)}")
        print(f"Summary file: {summary_path}")
        
        return save_path
    
    def list_saved_sessions(self) -> list:
        """List all saved test sessions"""
        sessions = []
        if os.path.exists(self.base_dir):
            for item in os.listdir(self.base_dir):
                item_path = os.path.join(self.base_dir, item)
                if os.path.isdir(item_path) and not item.startswith('.'):
                    sessions.append({
                        'name': item,
                        'path': item_path,
                        'created': datetime.fromtimestamp(os.path.getctime(item_path))
                    })
        
        # Sort by creation time (newest first)
        sessions.sort(key=lambda x: x['created'], reverse=True)
        return sessions
    
    def cleanup_old_sessions(self, keep_count: int = 5):
        """Clean up old test sessions, keeping only the most recent ones"""
        sessions = self.list_saved_sessions()
        
        if len(sessions) <= keep_count:
            print(f"Only {len(sessions)} sessions found. Keeping all.")
            return
        
        # Remove oldest sessions
        for session in sessions[keep_count:]:
            try:
                shutil.rmtree(session['path'])
                print(f"Removed old session: {session['name']}")
            except Exception as e:
                print(f"Error removing session {session['name']}: {e}")
        
        print(f"Kept the most recent {keep_count} sessions.")
    
    def generate_report_index(self):
        """Generate an index file listing all saved sessions"""
        sessions = self.list_saved_sessions()
        
        index_path = os.path.join(self.base_dir, "index.md")
        with open(index_path, 'w') as f:
            f.write("# Matplotlib Test Results Index\n\n")
            f.write(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Total Sessions: {len(sessions)}\n\n")
            
            if sessions:
                f.write("## Recent Test Sessions\n\n")
                for i, session in enumerate(sessions[:10], 1):
                    f.write(f"### {i}. {session['name']}\n")
                    f.write(f"- **Created**: {session['created'].strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"- **Path**: `{session['path']}`\n")
                    
                    # List files in the session directory
                    if os.path.exists(session['path']):
                        files = os.listdir(session['path'])
                        f.write(f"- **Files**: {len(files)} files\n")
                        for file in sorted(files):
                            if file != 'session_summary.txt':
                                f.write(f"  - `{file}`\n")
                    f.write("\n")
            else:
                f.write("No saved sessions found.\n")
        
        print(f"Generated index file: {index_path}")
        return index_path


def save_all_generated_results(session_name: str = "matplotlib_tests"):
    """
    Convenience function to save all currently generated results
    
    Args:
        session_name: Name for this test session
        
    Returns:
        str: Path to the saved results directory
    """
    saver = ResultSaver()
    saved_path = saver.save_current_results(session_name)
    
    # Generate index
    saver.generate_report_index()
    
    return saved_path


if __name__ == "__main__":
    print("Saving all generated matplotlib results...")
    
    # Save current results
    saved_path = save_all_generated_results("comprehensive_test")
    
    # List all sessions
    saver = ResultSaver()
    sessions = saver.list_saved_sessions()
    
    print(f"\nAll saved sessions:")
    for session in sessions[:5]:  # Show last 5
        print(f"  - {session['name']} ({session['created'].strftime('%Y-%m-%d %H:%M:%S')})")
    
    print(f"\nResults saved successfully!")
    print(f"Main directory: {saver.base_dir}")
    print(f"Latest session: {saved_path}")
