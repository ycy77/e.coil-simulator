---
entity_id: "gene.b2907"
entity_type: "gene"
name: "ubiH"
source_database: "NCBI RefSeq"
source_id: "gene-b2907"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2907"
  - "ubiH"
---

# ubiH

`gene.b2907`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2907`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiH (gene.b2907) is a gene entity. It encodes ubiH (protein.P25534). Encoded protein function: FUNCTION: Is likely an oxygenase that introduces the hydroxyl group at carbon four of 2-octaprenyl-6-methoxyphenol resulting in the formation of 2-octaprenyl-6-methoxy-1,4-benzoquinol. {ECO:0000269|PubMed:4572721}. EcoCyc product frame: OCTAPRENYL-METHOXYPHENOL-OH-MONOMER. EcoCyc synonyms: acd, visB. Genomic coordinates: 3052340-3053518. EcoCyc protein note: ubiH is thought to encode 2-octaprenyl-6-methoxyphenol 4-hydroxylase, one of the aerobic hydroxylases in the ubiquinone biosynthesis pathway. No direct biochemical evidence for the enzymatic activity of UbiH exists to date. UbiH is a component of the Ubi complex metabolon . UbiH predominantly localizes to the cytosol. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol. UbiH is predicted to contain FAD . Mutants in ubiH accumulate 2-octaprenyl-6-methoxyphenol ; accumulation of this compound may be the cause of the visible light sensitive phenotype of ubiH mutants . ubiH mutants are unable to grow on succinate or glycerol as the sole source of carbon. Inactivation of ubiH results in dependence on an intact RecA...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25534|protein.P25534]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ubiH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009545,ECOCYC:EG11324,GeneID:947388`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3052340-3053518:-; feature_type=gene
