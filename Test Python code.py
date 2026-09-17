
from loguru import logger

labour_with_cost = {"Mahesh":500, "Ramesh":400, "Mithilesh":400, "Sumesh":300}

# Update the dictionary # if key is not present then it will add the key and value in the dictionary
labour_with_cost["Jagmohan"] = 1000
labour_with_cost["Mahesh"] = 800

logger.info(labour_with_cost)