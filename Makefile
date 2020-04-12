deploy:
	aws cloudformation package \
		--template-file template.yaml \
		--output-template-file packaged-template.yaml \
		--s3-bucket ${CODERCAVE_BUCKET} \
		--profile caveman

	$(info [+] Deploying 'codercave-python-runtime-upgrade')
	aws cloudformation deploy \
		--template-file packaged-template.yaml \
		--stack-name codercave-python-runtime-upgrade \
		--capabilities CAPABILITY_IAM \
		--profile caveman

delete:
	aws cloudformation delete-stack \
		--stack-name codercave-python-runtime-upgrade \
		--profile caveman