---
entity_id: "gene.b0123"
entity_type: "gene"
name: "cueO"
source_database: "NCBI RefSeq"
source_id: "gene-b0123"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0123"
  - "cueO"
---

# cueO

`gene.b0123`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0123`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cueO (gene.b0123) is a gene entity. It encodes cueO (protein.P36649). Encoded protein function: FUNCTION: Multicopper oxidase involved in copper homeostasis and copper tolerance under aerobic conditions (PubMed:11222619, PubMed:11399769, PubMed:11527384, PubMed:15516598). Is responsible for the oxidation of Cu(+) to the less harmful Cu(2+) in the periplasm, thereby preventing Cu(+) from entering the cytoplasm (PubMed:15516598, PubMed:20088522, PubMed:25679350). Probably primarily functions as a cuprous oxidase in vivo (PubMed:20088522). {ECO:0000269|PubMed:11222619, ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:11527384, ECO:0000269|PubMed:15516598, ECO:0000269|PubMed:20088522, ECO:0000269|PubMed:25679350}.; FUNCTION: In vitro, in the presence of excess copper ions, exhibits ferroxidase and phenoloxidase activities (PubMed:11466290, PubMed:11527384, PubMed:11867755, PubMed:15317788, PubMed:15516598, PubMed:17804014, PubMed:25679350). Fe(2+) is an excellent substrate in the presence of excess Cu(2+), but is inactive in the absence of Cu(2+) (PubMed:15516598, PubMed:17804014). Oxidizes the phenolate iron siderophores enterobactin, 2,3-dihydroxybenzoate (2,3-DHB) and 3-hydroxyanthranilate (3-HAA) (PubMed:11466290, PubMed:15317788)...

## Biological Role

Activated by cueR (protein.P0A9G4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36649|protein.P36649]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9G4|protein.P0A9G4]] `RegulonDB` `C` - regulator=CueR; target=cueO; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000430,ECOCYC:EG12318,GeneID:947736`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:137083-138633:+; feature_type=gene
