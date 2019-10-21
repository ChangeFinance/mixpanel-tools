from mixpanel_api import Mixpanel

import authentication

if __name__ == '__main__':
	mixpanel = Mixpanel(authentication.api_secret, token=authentication.token)
	deleted_count = mixpanel.people_delete(query_params={'selector': 'user["$email"]==""'})
	print(deleted_count)
