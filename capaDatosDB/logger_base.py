import logging as log


log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)s] - %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p',
    handlers=[
        log.FileHandler('capa_datos.log'),
        log.StreamHandler()
    ]
)

if __name__ == '__main__':
    log.debug('mensaje a nivel de DEBUG')
    log.info('mensaje a nivel de info')
    log.warning('mensaje a nivel de wargning')
    log.error('mensaje a nivel de error')
    log.critical('mensaje a nivel de critical')
