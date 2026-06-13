---
entity_id: "gene.b0088"
entity_type: "gene"
name: "murD"
source_database: "NCBI RefSeq"
source_id: "gene-b0088"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0088"
  - "murD"
---

# murD

`gene.b0088`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0088`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murD (gene.b0088) is a gene entity. It encodes murD (protein.P14900). Encoded protein function: FUNCTION: Cell wall formation (Probable). Catalyzes the addition of glutamate to the nucleotide precursor UDP-N-acetylmuramoyl-L-alanine (UMA) (PubMed:1765076). {ECO:0000269|PubMed:1765076, ECO:0000305}. EcoCyc product frame: UDP-NACMURALA-GLU-LIG-MONOMER. Genomic coordinates: 97087-98403. EcoCyc protein note: UDP-N-acetylmuramoyl-L-alanine:D-glutamate ligase (MurD) catalyzes the addition of the second amino acid to the peptide moiety of the monomer unit of peptidoglycan. There are estimated to be less than 1000 copies of MurD in the cell . Biosynthesis of the cytoplasmic precursor subunit of peptidoglycan has been reconstituted in vitro . The reaction mechanism and specific inhibitors of the enzyme have been studied . In vitro in the absence of D-glutamate, MurD can catalyze the formation of p4A from ATP via an acyl phosphate intermediate . Crystal structures of the enzyme alone and in complex with substrates, product or inhibitors have been solved, and a catalytic mechanism involving an acyl phosphate intermediate was deduced . Results from site-directed mutagenesis of conserved amino acid residues within the active site correlated with their assigned function based on the crystal structures...

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186). Activated by glaR (protein.P37338).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P14900|protein.P14900]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=murD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=murD; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=murD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000318,ECOCYC:EG10620,GeneID:944818`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:97087-98403:+; feature_type=gene
