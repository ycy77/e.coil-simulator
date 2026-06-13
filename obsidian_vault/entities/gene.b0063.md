---
entity_id: "gene.b0063"
entity_type: "gene"
name: "araB"
source_database: "NCBI RefSeq"
source_id: "gene-b0063"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0063"
  - "araB"
---

# araB

`gene.b0063`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0063`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

araB (gene.b0063) is a gene entity. It encodes araB (protein.P08204). Encoded protein function: Ribulokinase (EC 2.7.1.16) EcoCyc product frame: RIBULOKIN-MONOMER. Genomic coordinates: 68348-70048. EcoCyc protein note: Ribulokinase catalyzes the phosphorylation of L-ribulose to L-ribulose-5-phosphate, the second step in the L-arabinose degradation pathway. The araBAD operon and its gene products were first studied in E. coli B/r . The E. coli B ribulokinase has been purified and crystallized , and its subunit structure was determined . The enzyme uses four 2-ketopentoses (L- and D-ribulose, L- and D-xylulose) with similar catalytic activity. In addition, L-arabitol and ribitol can serve as substrates . In the absence of sugar substrates, the enzyme exhibits a low ATPase activity . The sequence of the E. coli B enzyme is 98% identical to the E. coli K-12 enzyme. Transcription of the araBAD operon is induced in the presence of L-arabinose by the transcription factor AraC . araBAD expression can also induced by L-lyxose . araB mutants can not utilize L-arabinose for growth .

## Biological Role

Repressed by araC (protein.P0A9E0). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), rpoD (protein.P00579), fur (protein.P0A9A9), araC (protein.P0A9E0), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08204|protein.P08204]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=araB; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=araB; function=+
- `activates` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `C` - regulator=AraC; target=araB; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=araB; function=+
- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `C` - regulator=AraC; target=araB; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0000223,ECOCYC:EG10053,GeneID:946017`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:68348-70048:-; feature_type=gene
