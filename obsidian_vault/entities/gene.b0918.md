---
entity_id: "gene.b0918"
entity_type: "gene"
name: "kdsB"
source_database: "NCBI RefSeq"
source_id: "gene-b0918"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0918"
  - "kdsB"
---

# kdsB

`gene.b0918`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0918`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdsB (gene.b0918) is a gene entity. It encodes kdsB (protein.P04951). Encoded protein function: FUNCTION: Activates KDO (a required 8-carbon sugar) for incorporation into bacterial lipopolysaccharide in Gram-negative bacteria. {ECO:0000255|HAMAP-Rule:MF_00057}. EcoCyc product frame: CPM-KDOSYNTH-MONOMER. Genomic coordinates: 970852-971598. EcoCyc protein note: CMP-KDO synthetase activates the 8-carbon sugar KDO for incorporation into lipopolysaccharide. The β-pyranose form of KDO is the preferred substrate of CMP-KDO synthetase . A nucleophilic displacement mechanism was proposed for the enzyme . Based on kinetic, modelling and EPR studies and the crystal structure of the ternary complex, a reaction mechanism involving two Mg2+ ions was proposed . A crystal structure of the enzyme has been solved at 2.6 Å resolution ; the structure of the ternary complex of KdsB with CTP and 2β-deoxy KDO was solved at 1.9 Å resolution . Expression of kdsB is growth regulated: it is highest in early log phase and decreases in stationary phase . kdsB is an essential gene .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04951|protein.P04951]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kdsB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003122,ECOCYC:EG10519,GeneID:945539`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:970852-971598:+; feature_type=gene
