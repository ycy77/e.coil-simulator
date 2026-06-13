---
entity_id: "gene.b2256"
entity_type: "gene"
name: "arnD"
source_database: "NCBI RefSeq"
source_id: "gene-b2256"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2256"
  - "arnD"
---

# arnD

`gene.b2256`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2256`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arnD (gene.b2256) is a gene entity. It encodes arnD (protein.P76472). Encoded protein function: FUNCTION: Catalyzes the deformylation of 4-deoxy-4-formamido-L-arabinose-phosphoundecaprenol to 4-amino-4-deoxy-L-arabinose-phosphoundecaprenol. The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides (Probable). {ECO:0000305|PubMed:15695810}. EcoCyc product frame: G7169-MONOMER. EcoCyc synonyms: pmrJ, yfbH. Genomic coordinates: 2370018-2370908. EcoCyc protein note: ArnD is predicted to act as a deformylase that removes the formyl group from undecaprenyl phosphate-L-Ara4FN . Deletion of arnD results in restoration of polymyxin sensitivity in a polymyxin-resitant pmrAc strain . Expression of the arnBCADTEF operon increased during growth with elevated FeSO4, FeCl3, or ZnSO4 and was dependent upon the BasSR two-component signal transduction system .

## Biological Role

Activated by basR (protein.P30843).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76472|protein.P76472]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=arnD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007462,ECOCYC:G7169,GeneID:945334`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2370018-2370908:+; feature_type=gene
