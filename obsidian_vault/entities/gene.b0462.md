---
entity_id: "gene.b0462"
entity_type: "gene"
name: "acrB"
source_database: "NCBI RefSeq"
source_id: "gene-b0462"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0462"
  - "acrB"
---

# acrB

`gene.b0462`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0462`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acrB (gene.b0462) is a gene entity. It encodes acrB (protein.P31224). Encoded protein function: FUNCTION: The inner membrane transporter component of the AcrAB-TolC efflux system which confers multidrug resistance (PubMed:16915237, PubMed:16946072, PubMed:17194213, PubMed:23010927, PubMed:28355133, PubMed:31201302). The AcrAB-TolC efflux system has a broad substrate specificity, acting as a substrate:proton antiporter, using proton motive force to export substrates (PubMed:16915237, PubMed:16946072, PubMed:17015667, PubMed:17194213, PubMed:19023693, PubMed:19425588, PubMed:22121023, PubMed:23010927, PubMed:25248080). Oxidized fatty acids may be one class of native substrate for AcrB, as part of the AcrAB-TolC efflux protein complex (PubMed:33785633). AcrB is also a component of the AcrABZ-TolC efflux system, where the small accessory protein AcrZ, together with membrane lipids, may influence the specificity of drug export (PubMed:23010927, PubMed:24747401, PubMed:32348749). {ECO:0000269|PubMed:16915237, ECO:0000269|PubMed:16946072, ECO:0000269|PubMed:17015667, ECO:0000269|PubMed:17194213, ECO:0000269|PubMed:19023693, ECO:0000269|PubMed:19425588, ECO:0000269|PubMed:22121023, ECO:0000269|PubMed:23010927, ECO:0000269|PubMed:24747401, ECO:0000269|PubMed:25248080, ECO:0000269|PubMed:28355133, ECO:0000269|PubMed:31201302, ECO:0000269|PubMed:32348749, ECO:0000269|PubMed:33785633}...

## Biological Role

Repressed by acrR (protein.P0ACS9), envR (protein.P0ACT2). Activated by soxS (protein.P0A9E2), marA (protein.P0ACH5), rob (protein.P0ACI0).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31224|protein.P31224]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=acrB; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=acrB; function=+
- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `RegulonDB` `S` - regulator=Rob; target=acrB; function=+
- `represses` <-- [[protein.P0ACS9|protein.P0ACS9]] `RegulonDB` `C` - regulator=AcrR; target=acrB; function=-
- `represses` <-- [[protein.P0ACT2|protein.P0ACT2]] `RegulonDB` `S` - regulator=EnvR; target=acrB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001601,ECOCYC:EG11704,GeneID:945108`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:481254-484403:-; feature_type=gene
