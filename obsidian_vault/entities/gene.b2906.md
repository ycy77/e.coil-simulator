---
entity_id: "gene.b2906"
entity_type: "gene"
name: "ubiI"
source_database: "NCBI RefSeq"
source_id: "gene-b2906"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2906"
  - "ubiI"
---

# ubiI

`gene.b2906`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2906`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiI (gene.b2906) is a gene entity. It encodes ubiI (protein.P25535). Encoded protein function: FUNCTION: FAD-dependent monooxygenase required for the aerobic hydroxylation of 2-octaprenylphenol to 2-octaprenyl-6-hydroxy-phenol, the first hydroxylation step in coenzyme Q (ubiquinone) biosynthesis. {ECO:0000269|PubMed:23709220}. EcoCyc product frame: EG11333-MONOMER. EcoCyc synonyms: visC. Genomic coordinates: 3051115-3052317. EcoCyc protein note: UbiI is a component of the Ubi complex metabolon . UbiI functions in the hydroxylation of the C5 position during the aerobic biosynthesis of ubiquinone-8. UbiI predominantly localizes to the cytosol. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol . Purified UbiI is unstable; an inactive truncated form was isolated and behaves like a tetramer in solution. The crystal structure of this protein has been solved at 2.0 Å resolution. Point mutants in the predicted FAD binding site do not complement a ΔubiI mutant . Deletion of ubiI (visC) has no effect on photosensitivity or aerobic respiration ; however, a ubiI mutant strain contains only 7% of wild type levels of ubiquinone-8 and accumulates 3-octaprenyl-4-hydroxyphenol (4-HP8) . The residual C5 hydroxylase activity appears to be provided by UbiF...

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

- `encodes` --> [[protein.P25535|protein.P25535]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ubiI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009543,ECOCYC:EG11333,GeneID:947389`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3051115-3052317:-; feature_type=gene
