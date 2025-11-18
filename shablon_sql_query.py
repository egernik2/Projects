def add_values_to_geoip_table(self, id_src_dst_list):
        if not id_src_dst_list:
            return
        with self._conn:
            with self._conn.cursor() as cur:
                query = "INSERT INTO tgeo (msg_id, src_country, src_iso_code, src_city, src_lat, src_long, " \
                        "dst_country, dst_iso_code, dst_city, dst_lat, dst_long) VALUES {};".format(
                    ", ".join(["%s"]*len(id_src_dst_list)))
                cur.execute(query, id_src_dst_list)
        log.info("Values added to tgeo table. Last msg_id={}".format(max((x[0] for x in id_src_dst_list))))