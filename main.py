import pyautogui, os, time, sys
import threading
from itertools import cycle

# Enhanced Spinner Class for the automation
class AutomationSpinner:
    def __init__(self, chars=['|', '/', '-', '\\'], delay=0.1):
        self.chars = chars
        self.delay = delay
        self.running = False
        self.thread = None
        self.current_message = ""
        self.step_count = 0
        self.total_steps = 0
    
    def _spin(self):
        """The spinning animation loop"""
        spinner = cycle(self.chars)
        while self.running:
            spin_char = next(spinner)
            if self.total_steps > 0:
                progress = f"[{self.step_count}/{self.total_steps}]"
                print(f'\r{self.current_message} {spin_char} {progress}', end='', flush=True)
            else:
                print(f'\r{self.current_message} {spin_char}', end='', flush=True)
            time.sleep(self.delay)
    
    def start(self, message="Processing", total_steps=0):
        """Start the spinner with a message"""
        self.current_message = message
        self.total_steps = total_steps
        self.step_count = 0
        self.running = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.daemon = True
        self.thread.start()
    
    def update_message(self, message, step=None):
        """Update the spinner message"""
        self.current_message = message
        if step is not None:
            self.step_count = step
    
    def stop(self, final_message="Complete!"):
        """Stop the spinner"""
        self.running = False
        if self.thread:
            self.thread.join()
        print(f'\r{final_message}' + ' ' * 20)  # Clear any remaining characters

# Global spinner instance
spinner = AutomationSpinner()

# MOUSE CONTROL
duration = 1

def method1_try_except():
    """Exit loop with Ctrl+C using try-except"""
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Current mouse position: ({x}, {y})")
            time.sleep(0.1)  # Small delay to prevent spam
    except KeyboardInterrupt:
        print("\nExiting... Ctrl+C pressed")
        sys.exit(0)

def set_trimester(title, isChild, arrowDown, step_num, total_steps):
    """Enhanced function with spinner updates"""
    spinner.update_message(" ", step_num)
    
    # reset to position
    pyautogui.moveTo(1952, 697)
    pyautogui.scroll(1000)
    
    # click add
    spinner.update_message(" ", step_num)
    pyautogui.click(2266, 725)
    time.sleep(duration)
    
    # click add category
    spinner.update_message(" ",step_num)
    pyautogui.press('down', 2)
    pyautogui.press('enter')
    time.sleep(duration+1)
    
    # click title textbox and enter title
    spinner.update_message(" ", step_num)
    pyautogui.press('tab')
    time.sleep(duration)
    pyautogui.press('tab')
    time.sleep(duration)
    pyautogui.write(title)
    time.sleep(duration+1)
    pyautogui.scroll(-1000)
    
    if (isChild):
        # click parent category 
        spinner.update_message(" ", step_num)
        time.sleep(duration)
        pyautogui.click(1479,1052)
        time.sleep(duration)
        pyautogui.press('down', presses=arrowDown)
        pyautogui.press('enter')
    
    # Save and continue
    spinner.update_message(" ", step_num)
    time.sleep(duration)
    pyautogui.click(2440,1282)
    time.sleep(duration+2)
    
    # click continue when recalculating grades
    spinner.update_message(" ", step_num)
    pyautogui.click(1930, 843)
    time.sleep(duration+3)
    
    spinner.update_message(" ", step_num)

def main():
    """Main execution function with enhanced spinner"""
    os.system('cls')
    
    print("🚀 AUTOMATION SCRIPT STARTING")
    print("=" * 50)
    print("⚠️  DO NOT TOUCH YOUR PC DURING EXECUTION")
    print("⚠️  Press Ctrl+C to stop if needed")
    print("=" * 50)
    print()
    
    # Define all tasks
    tasks = [
        ("1st Trimester", False, 0),
        ("2nd Trimester", False, 0),
        ("3rd Trimester", False, 0),
        ("1st Trimester Written Works", True, 1),
        ("1st Trimester Performance Tasks", True, 1),
        ("2nd Trimester Written Works", True, 2),
        ("2nd Trimester Performance Tasks", True, 2),
        ("3rd Trimester Written Works", True, 3),
        ("3rd Trimester Performance Tasks", True, 3)
    ]
    
    total_steps = len(tasks)
    
    try:
        # Start the spinner
        spinner.start(" ", total_steps)
        time.sleep(1)
        
        # Process parent trimesters
        spinner.update_message(" ",0)
        for i in range(3):
            title, isChild, arrowDown = tasks[i]
            set_trimester(title, isChild, arrowDown, i + 1, total_steps)
        
        spinner.update_message(" ", 3)
        time.sleep(1)
        
        # Process child categories
        spinner.update_message(" ",3)
        for i in range(3, 9):
            title, isChild, arrowDown = tasks[i]
            set_trimester(title, isChild, arrowDown, i + 1, total_steps)
        
        # Final summary
        os.system('cls')
        print("🎊 AUTOMATION COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        print("✅ Created 3 parent trimesters")
        print("✅ Created 6 child categories")
        print("✅ All grade categories configured")
        print("=" * 50)
        print("🎯 Your gradebook is now ready to use!")
        
    except KeyboardInterrupt:
        spinner.stop("❌ AUTOMATION STOPPED BY USER")
        print("\n🛑 Script interrupted by user (Ctrl+C)")
        print("⚠️  Some trimesters may not be fully configured")
        sys.exit(0)
    except Exception as e:
        spinner.stop("❌ ERROR OCCURRED")
        print(f"\n💥 An error occurred: {str(e)}")
        print("⚠️  Please check your screen resolution and application state")
        sys.exit(1)

def show_position_tracker():
    """Show mouse position tracker with spinner"""
    print("🎯 MOUSE POSITION TRACKER")
    print("=" * 30)
    print("Use this to find coordinates for automation")
    print("Press Ctrl+C to exit")
    print("=" * 30)
    
    spinner.start("🔍 Tracking mouse position")
    
    try:
        while True:
            x, y = pyautogui.position()
            spinner.update_message(f"🔍 Mouse at: ({x}, {y})")
            time.sleep(0.1)
    except KeyboardInterrupt:
        spinner.stop("👋 Position tracking stopped")
        print("\nExiting position tracker...")
        sys.exit(0)

if __name__ == "__main__":
    print("🤖 TRIMESTER AUTOMATION SCRIPT")
    print("=" * 40)
    print("1. Run automation")
    print("2. Track mouse position")
    print("=" * 40)
    
    choice = input("Choose option (1-2): ").strip()
    
    if choice == "1":
        main()
    elif choice == "2":
        show_position_tracker()
    else:
        print("❌ Invalid choice. Running automation...")
        main()
