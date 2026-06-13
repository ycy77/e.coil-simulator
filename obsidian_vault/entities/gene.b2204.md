---
entity_id: "gene.b2204"
entity_type: "gene"
name: "napH"
source_database: "NCBI RefSeq"
source_id: "gene-b2204"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2204"
  - "napH"
---

# napH

`gene.b2204`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2204`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

napH (gene.b2204) is a gene entity. It encodes napH (protein.P33934). Encoded protein function: FUNCTION: Required for electron transfer from ubiquinol, via NapC, to the periplasmic nitrate reductase NapAB complex. {ECO:0000269|PubMed:11967083, ECO:0000269|PubMed:14674886}. EcoCyc product frame: NAPH-MONOMER. EcoCyc synonyms: yejZ. Genomic coordinates: 2298715-2299578. EcoCyc protein note: The EG12062 gene encodes a ferredoxin-type non-heme iron-sulfur protein. . NapH is an integral membrane protein with four membrane-spanning domains; the C-terminal domain with its two predicted [4Fe-4S] clusters is located in the cytoplasm . Using two-hybrid assays, it has been shown that NapH interacts strongly with EG12060 NapC . A mutant lacking EG12064 and EG12062 was totally defective for growth in glycerol/nitrate medium. When grown in glucose/nitrate medium, it was found that the mutant had almost completely lost the ability to reduce nitrate. With ubiquinol as the electron donor no significant nitrate reduction could be observed . In a subsequent study, deletion of either EG12064 or EG12062 almost abolished Nap-dependent nitrate reduction by a strain uncapable of producing menaquinone. Thus it was concluded that NapG and NapH are required for electron transfer from ubiquinol, but not menaquinol, via EG12060 NapC, to the NAP-CPLX NapAB complex .

## Biological Role

Repressed by narL (protein.P0AF28), iscR (protein.P0AGK8), narP (protein.P31802). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33934|protein.P33934]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=napH; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=napH; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=napH; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napH; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=napH; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=napH; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napH; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007285,ECOCYC:EG12062,GeneID:945984`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2298715-2299578:-; feature_type=gene
