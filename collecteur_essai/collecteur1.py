"""Module Collecteur1

Presentation of collecteur1 which collects and sends data to the text file fichier.txt

Copyright (c) 2021 Melissa BENARD
All Rights Reserved.
Released under the MIT license

"""
import psutil
import time


def collect_data_text_file():
    """ Collect the system data
    """
    #
    # Open a text file fichier.txt and return it as an object
    # 2 params : name and mode ("a" add : to insert text in the end and not overwrite previous data)
    #
    file = open("fichier.txt", "a")
    #
    # Write a specified text in the opened text file fichier.txt
    # str() converts the value into string of the data
    #
    file.write("Le taux d'utilisation des CPUs est : " + str(psutil.cpu_percent(1)) + "% ;\n")

    file.write("Le taux d'utilisation de la mémoire est : " + str(psutil.virtual_memory().percent) + "% ;\n")

    file.write("Le taux d'occupation des disques est : " + str(psutil.disk_usage("/").percent) + "% ;\n")

    file.write("Le volume d'information transmis par les interfaces réseau est : " + str(
        psutil.net_io_counters().bytes_sent) + "octets ;\n")
    #
    # Display the current date and hour
    #
    file.write("-----------------------------" + str(time.ctime(time.time())) + "------------------------------\n")
    #
    # Close the opened text file fichier.txt
    #
    file.close()


def main():
    """The main function

    Executes the function collect_data_text_file() every 10 seconds
    """
    while True:
        try:
            collect_data_text_file()
            time.sleep(10)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
