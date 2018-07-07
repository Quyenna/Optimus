class Write:
    def json(self, path):
        """

        :param self:
        :param path:
        :return:
        """
        p = re.sub("}\'", "}", re.sub("\'{", "{", str(self._df.toJSON().collect())))

        with open(path, 'w') as outfile:
            # outfile.write(str(json_cols).replace("'", "\""))
            outfile.write(p)

    def csv(self, path_name, header="true", mode="overwrite", sep=",", *args, **kargs):
        """
        Write dataframe as CSV.
        :param path_name: Path to write the DF and the name of the output CSV file.
        :param header: True or False to include header
        :param mode: Specifies the behavior of the save operation when data already exists.
                    "append": Append contents of this DataFrame to existing data.
                    "overwrite" (default case): Overwrite existing data.
                    "ignore": Silently ignore this operation if data already exists.
                    "error": Throw an exception if data already exists.
        :param sep: sets the single character as a separator for each field and value. If None is set,
        it uses the default value.
        :return: Dataframe in a CSV format in the specified path.
        """

        self._assert_type_str(path_name, "path_name")

        assert header == "true" or header == "false", "Error header must be 'true' or 'false'"

        if header == 'true':
            header = True
        else:
            header = False

        return self._df.write.options(header=header).mode(mode).csv(path_name, sep=sep, *args, **kargs)