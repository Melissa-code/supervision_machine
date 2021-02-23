"""Module collecteur_db

Presentation du collecteur_db which collects and sends data to the database Phpmyadmin

Copyright (c) 2021 Melissa BENARD
All Rights Reserved.
Released under the MIT license

"""
import psutil
import time
import mysql.connector


def get_cpu_percent():
    """Collect cpu usage in percent

    Returns: Usage ratio of CPUs
    """
    return psutil.cpu_percent(1)


def get_virtual_memory():
    """Get the virtual memory stats

    Returns: The virtual memory stats

    Available fields: total, available, percent, used, free
    """
    my_stats_memory = [psutil.virtual_memory().total,
                       psutil.virtual_memory().available,
                       psutil.virtual_memory().percent,
                       psutil.virtual_memory().used,
                       psutil.virtual_memory().free
                       ]
    return my_stats_memory


def get_disk_usage():
    """Get the disk usage stats

    Returns: The disk usage stats

    Available fields: total, used, free, percent
    """
    my_stats_disk = [
        psutil.disk_usage("/").total,
        psutil.disk_usage("/").used,
        psutil.disk_usage("/").free,
        psutil.disk_usage("/").percent
    ]
    return my_stats_disk


def get_net_io_counters():
    """Get the sent bytes counter

    """
    bytes_sent_value = psutil.net_io_counters().bytes_sent
    return bytes_sent_value


def collect_to_phpmyadmin(sql_statement):
    """Write to the database

    Args:
        sql_statement (str) sql statement to execute
    """
    #
    # Connexion to database Phpmyadmin
    #
    try:
        print(sql_statement)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="infosystem",
            port="8889"
        )
    #
    # Display an error message if no connexion
    #
    except mysql.Error as e:
        print(f"Error connecting to mysql: {e}")
        return
    #
    # Create a cursor
    #
    mycursor = connection.cursor()
    #
    # Execute Sql statement
    #
    mycursor.execute(sql_statement)
    #
    # Commit on the database
    #
    connection.commit()
    # print(mycursor.rowcount, "record inserted")
    #
    # Close the connection to the database
    #
    connection.close()


def main():
    """The main function
    """
    while True:
        try:
            #
            # Suspend the execution for 10 seconds
            #
            time.sleep(10)
            #
            # Get the CPU percent
            #
            cpu = get_cpu_percent()
            #
            # Get the virtual memory stats
            #
            memory = get_virtual_memory()
            #
            # Get the disk usage stats
            #
            disk = get_disk_usage()
            #
            # Get the sent bytes net io counters
            #
            counters = get_net_io_counters()
            #
            # Insert the cpu percent into the database
            #
            sql_statement = f"INSERT INTO cpu_percent " \
                            f"(counter) " \
                            f"VALUES " \
                            f"({cpu})"
            collect_to_phpmyadmin(sql_statement)
            #
            # Insert the memory stats into the database
            #
            sql_statement = f"INSERT INTO virtual_memory " \
                            f"(total_memory, available_memory, percent_memory, used_memory, free_memory) " \
                            f"VALUES " \
                            f"({memory[0]},{memory[1]},{memory[2]},{memory[3]},{memory[4]})"
            collect_to_phpmyadmin(sql_statement)
            #
            # Insert the disk stats into the database
            #
            sql_statement = f"INSERT INTO disk_usage " \
                            f"(total_disk, used_disk, free_disk, percent_disk) " \
                            f"VALUES " \
                            f"({disk[0]},{disk[1]},{disk[2]},{disk[3]})"
            collect_to_phpmyadmin(sql_statement)
            #
            # Insert the io sent bytes into the database
            #
            sql_statement = f"INSERT INTO io_counters_sent_bytes " \
                            f"(counter_io_sentbytes) " \
                            f"VALUES " \
                            f"({counters})"
            collect_to_phpmyadmin(sql_statement)

        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
