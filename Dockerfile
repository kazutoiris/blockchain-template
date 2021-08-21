FROM cjlu/blockchainenv:latest

ENV tag_name="v0.5.10"

COPY ./eth.sol /root/ethbot/eth.sol
COPY ./custom.py /root/ethbot/custom.py

RUN chmod +x /root/ethbot/*.py && \
    /usr/bin/python3 /inst.py && \
    chmod 0777 /root/.solcx/* && \
    rm -rf /inst.py

CMD ["/start.sh"]

EXPOSE 9999
