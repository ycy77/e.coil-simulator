---
entity_id: "gene.b2994"
entity_type: "gene"
name: "hybC"
source_database: "NCBI RefSeq"
source_id: "gene-b2994"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2994"
  - "hybC"
---

# hybC

`gene.b2994`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2994`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hybC (gene.b2994) is a gene entity. It encodes hybC (protein.P0ACE0). Encoded protein function: FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD2 is involved in hydrogen uptake. EcoCyc product frame: HYBC-MONOMER. Genomic coordinates: 3141286-3142989. EcoCyc protein note: HybC is the large, [NiFe]-containing subunit of hydrogenase 2. The nickel and iron atoms are coordinated by 4 Cys thiolates plus 3 diatomic ligands (2 cyano and a carbonyl). Acquisition of a [NiFe] cofactor, C-terminal processing of HybC and subsequent association with the small subunit (HybO) are required prior to export by the Tat system (and reviewed in . The maturation of the HybC protein was affected in a hypA mutant and a hypA slyD double mutant .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACE0|protein.P0ACE0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=hybC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009828,ECOCYC:EG11801,GeneID:945182`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3141286-3142989:-; feature_type=gene
