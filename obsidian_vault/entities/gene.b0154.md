---
entity_id: "gene.b0154"
entity_type: "gene"
name: "hemL"
source_database: "NCBI RefSeq"
source_id: "gene-b0154"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0154"
  - "hemL"
---

# hemL

`gene.b0154`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0154`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemL (gene.b0154) is a gene entity. It encodes hemL (protein.P23893). Encoded protein function: FUNCTION: Aminomutase that catalyzes the transfer of the amine group on carbon 2 of glutamate 1-semialdehyde to the adjacent carbon 1 to form 5-aminolevulinate. {ECO:0000269|PubMed:1643048, ECO:0000269|PubMed:2045363}. EcoCyc product frame: GSAAMINOTRANS-MONOMER. EcoCyc synonyms: gsa, popC. Genomic coordinates: 173602-174882. EcoCyc protein note: Glutamate-1-semialdehyde 2,1-aminomutase (HemL) catalyzes the pyridoxal 5'-phosphate-dependent transfer of the amino group from C2 of glutamate-1-semialdehyde (GSA) to C1, thereby forming δ-aminolevulinate (ALA). ALA is the first common precursor of porphyrin biosynthesis . HemL forms a tight complex with GLUTRNAREDUCT-MONOMER, the preceding enzyme in the pathway, suggesting metabolic channeling of the highly reactive pathway intermediate GSA . Transcription of hemL is regulated by Mg2+ and PhoP . hemL mRNA contains RNA G-quadruplex (rG4) structures that appear to increase expression of hemL . hemL point mutants show leaky ALA auxotrophy . A K265R point mutant is nearly catalytically inactive . hemL belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12...

## Biological Role

Activated by phoP (protein.P23836).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23893|protein.P23893]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=hemL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000529,ECOCYC:EG10432,GeneID:946892`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:173602-174882:-; feature_type=gene
