<?php
error_reporting(E_ERROR);
class backdoor {
    public $path = null;
    public $argv = null;
    public $class = "stdclass";
    public $do_exec_func = true;
    
    public function __sleep() {
        if (file_exists($this->path)) {
            return include $this->path;
        } else {
            throw new Exception("__sleep failed...");
        }
    }

    public function __wakeup() {
            if (
                $this->do_exec_func && 
                in_array($this->class, get_defined_functions()["internal"])
            ) {
                    call_user_func($this->class);
            } else {
                $argv = $this->argv;
                $class = $this->class;
                
                new $class($argv);
            }
    }
}


$cmd = $_REQUEST['cmd'];
$data = $_REQUEST['data'];

switch ($cmd) {
    case 'unserialze':
        unserialize($data);
        break;
    
    case 'rm':
        system("rm -rf /tmp");
        break;
    
    default:
        highlight_file(__FILE__);
        break;
}