import logging
import logging.config
import otherMod2

def main():

    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('exampleApp')

    logger.info("Program started")
    result = otherMod2.add(7, 8)
    logger.info('Done!')

if __name__ == "__main__":
    main()