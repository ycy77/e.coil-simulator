---
entity_id: "gene.b2367"
entity_type: "gene"
name: "emrY"
source_database: "NCBI RefSeq"
source_id: "gene-b2367"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2367"
  - "emrY"
---

# emrY

`gene.b2367`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2367`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

emrY (gene.b2367) is a gene entity. It encodes emrY (protein.P52600). Encoded protein function: FUNCTION: Part of the tripartite efflux system EmrYK-TolC, which confers resistance to various drugs. {ECO:0000250}. EcoCyc product frame: EMRY-MONOMER. Genomic coordinates: 2480638-2482176. EcoCyc protein note: EmrY is the inner membrane subunit of a putative tripartite efflux pump complex. EmrY is a member of the Drug:H+ Antiporter-2 (14 Spanner) (DHA2) Family within the Major Facilitator Superfamily (MFS) . EmrY has 63.3 % sequence identity with the efflux pump protein EMRB-MONOMER "EmrB" . emrY was identified in a screen for genes that reduce the lethal effects of stress; an emrY insertion mutant is more sensitive than wild type to mitomycin C and other stresses such as UV irradiation . emrY is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Activated by evgA (protein.P0ACZ4).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52600|protein.P52600]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=emrY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007806,ECOCYC:EG13283,GeneID:946835`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2480638-2482176:-; feature_type=gene
