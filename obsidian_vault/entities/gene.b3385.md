---
entity_id: "gene.b3385"
entity_type: "gene"
name: "gph"
source_database: "NCBI RefSeq"
source_id: "gene-b3385"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3385"
  - "gph"
---

# gph

`gene.b3385`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3385`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gph (gene.b3385) is a gene entity. It encodes gph (protein.P32662). Encoded protein function: FUNCTION: Specifically catalyzes the dephosphorylation of 2-phosphoglycolate (2P-Gly). Is involved in the dissimilation of the intracellular 2-phosphoglycolate formed during the DNA repair of 3'-phosphoglycolate ends, a major class of DNA lesions induced by oxidative stress. {ECO:0000269|PubMed:16990279}. EcoCyc product frame: GPH-MONOMER. EcoCyc synonyms: yhfE. Genomic coordinates: 3513631-3514389. EcoCyc protein note: The gph gene encodes a haloacid dehalogenase (HAD)-like phosphatase family enzyme with 2-phosphoglycolate phosphatase activity . 2-phosphoglycolate phosphatase is an enzyme of the Calvin Cycle for assimilation of CO2, and it was thus not clear why it would be found in E. coli . However, 2-phosphoglycolate is formed during repair of DNA strand breaks with 3'-phosphoglycolate ends; such breaks can be caused by radiomimetic drugs like bleomycin . Gph was shown to be involved in the recovery of glycolate from 2-phosphoglycolate released by the activity of DNA repair enzymes after bleomycin treatment . Deletion of gph resulted in loss of induction of the glc operon by glycolate after bleomycin treatment . gph mutants also failed to recover as quickly as wild type after bleomycin treatment . In a previous study gph deletion mutation had no apparent physiological effect...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32662|protein.P32662]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gph; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011058,ECOCYC:EG11871,GeneID:947895`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3513631-3514389:-; feature_type=gene
