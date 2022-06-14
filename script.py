import Saver


###Script###

class Runner:
    rool = Saver.Saver()
    start = rool.logs(f"____start_routine____")
    check_device = rool.new_device()
    copy = rool.copy_machine()
    check_copy_quality = rool.copy_quality()
    del_last_copy = rool.replace_old_copy()
    end = rool.logs("End of routine")


Run = Runner
Run()
