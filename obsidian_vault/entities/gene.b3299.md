---
entity_id: "gene.b3299"
entity_type: "gene"
name: "rpmJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3299"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3299"
  - "rpmJ"
---

# rpmJ

`gene.b3299`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3299`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpmJ (gene.b3299) is a gene entity. It encodes rpmJ (protein.P0A7Q6). Encoded protein function: FUNCTION: One of the last ribosomal proteins to be assembled in the 50S subunit, it contacts a number of helices in the 23S rRNA, acting as molecular glue (PubMed:33639093). The simultaneous presence of uL16 and bL36 probably triggers ObgE's GTPase activity and eventual dissociation from the mature 50S ribosomal subunit (PubMed:33639093). {ECO:0000269|PubMed:33639093}. EcoCyc product frame: EG11232-MONOMER. EcoCyc synonyms: secX. Genomic coordinates: 3442618-3442734. EcoCyc protein note: The L36 protein is a component of the 50S subunit of the ribosome . L36 is highly conserved in bacteria, mitochondria and chloroplasts, but not present in archaea and eukarya . Ribosomes lacking L36 are correctly assembled. However, chemical protection experiments suggest that rRNA tertiary interactions are disrupted in ribosomes lacking L36, thus arguing that L36 plays a significant role in organizing 23S rRNA structure . 2'-O-methylation of U2552 by EG11507-MONOMER promotes association between helices 92 and 71 of 23S rRNA; together with incorporation of L36, it promotes late steps of 50S ribosomal subunit assembly . Profiles of ribosomes isolated from a ΔrpmJ mutant show a minor peak at 40S that lacks the late assembly proteins L16 and L35...

## Biological Role

Repressed by rpsH (protein.P0A7W7).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7Q6|protein.P0A7Q6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rpmJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010812,ECOCYC:EG11232,GeneID:947805`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3442618-3442734:-; feature_type=gene
