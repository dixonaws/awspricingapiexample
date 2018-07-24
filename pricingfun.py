import awspricing
from awspricing import cache

awspricing.cache.AWSPRICING_USE_CACHE=1

ec2_offer = awspricing.offer('AmazonEC2')

ec2_offer.search_skus(
  instance_type='c4.large',
  location='US East (N. Virginia)',
  operating_system='Linux',
)  # {'4C7N4APU9GEUZ6H6', 'MBQPYDJSY3BY84BH', 'MDKVAJXMJGZFDJUE'}

fltC4LargePricing=ec2_offer.ondemand_hourly(
  'c4.large',
  operating_system='Linux',
  # lease_contract_length='3yr',
  # offering_class='standard',
  # purchase_option='Partial Upfront',
  region='us-east-1'
)  # 0.10845205479452055

print "Hourly c4.large pricing in us-east-1: $" + str(fltC4LargePricing)
