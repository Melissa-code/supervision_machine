"""Module collecteur_text

Presentation of collecteur_text which collects and sends data to the text file file.txt

Copyright (c) 2021 Melissa BENARD
All Rights Reserved.
Released under the MIT license

"""
import psutil
import time


def get_cpu_percent():
    """Collect cpu usage in percent

    Returns: Usage ration of CPUs
    """
    percent_cpu = psutil.cpu_percent(1)
    my_percent_cpu = "1. The usage ration of CPUs is : " + str(percent_cpu) + " %; \n"
    return "".join(my_percent_cpu)


def get_virtual_memory():
    """Get the virtual memory stats

    Returns: The virtual memory stats

    Available fields: total, available, percent, used, free
    """
    stats_memory = psutil.virtual_memory()
    my_stats_memory = [
        "2. The virtual memory stats are : \n" +
        " - total: " + str(stats_memory.total) + " octets, \n",
        " - available: " + str(stats_memory.available) + " octets, \n",
        " - percent: " + str(stats_memory.percent) + " %, \n",
        " - used: " + str(stats_memory.used) + " octets, \n",
        " - free: " + str(stats_memory.free) + " octets; \n"
    ]
    return "".join(my_stats_memory)


def get_disk_usage():
    """Get the disk usage stats

    Returns: The disk usage stats

    Available fields: total, used, free, percent
    """
    stats_disk = psutil.disk_usage("/")
    my_stats_disk = [
        "3. The disk usage stats are : \n" +
        " - total: " + str(stats_disk.total) + " octets, \n",
        " - used: " + str(stats_disk.used) + " octets, \n",
        " - free: " + str(stats_disk.free) + " octets, \n",
        " - percent: " + str(stats_disk.percent) + " %; \n"
    ]
    return "".join(my_stats_disk)


def get_net_io_counters():
    """Get the sent bytes counter

    """
    bytes_sent_value = psutil.net_io_counters().bytes_sent
    my_bytes_sent_value = "4. The value of the sent bytes counter is : " + str(bytes_sent_value) + " octets; \n"
    return "".join(my_bytes_sent_value)


def collect_to_text_file(text):
    """Write string into a file

    Args:
    text (str): the text to insert into the file

    Return: None
    """
    #
    # with is for a better errors management and closes automatically the text file
    # a+ to insert text in the end and not overwrite previous data
    #
    with open("file.txt", "a+") as file:
        file.write(text + "\n")


def get_time():
    """Get current time

        Args: None
        Return: None
        """
    #
    # Display current time
    #
    with open("file.txt", "a+") as file:
        file.write(
            "-----------------------------" + str(time.ctime(time.time())) + "------------------------------\n\n")


def main():
    """The main function
    """
    while True:
        try:
            #
            # Get current time
            #
            get_time()
            #
            # Get CPU percent
            #
            cpu = get_cpu_percent()
            file_line_cpu = f"{cpu} \n"
            collect_to_text_file(file_line_cpu)
            #
            # Get virtual memory stats
            #
            memory = get_virtual_memory()
            file_line_memory = f"{memory} \n"
            collect_to_text_file(file_line_memory)
            #
            # Get disk usage stats
            #
            disk = get_disk_usage()
            file_line_disk = f"{disk} \n"
            collect_to_text_file(file_line_disk)
            #
            # Get sent bytes net io counters
            #
            counters = get_net_io_counters()
            file_line_counters = f"{counters} \n"
            collect_to_text_file(file_line_counters)
            #
            # Suspend the execution for 10 seconds
            #
            time.sleep(10)

        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
