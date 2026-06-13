---
entity_id: "gene.b0086"
entity_type: "gene"
name: "murF"
source_database: "NCBI RefSeq"
source_id: "gene-b0086"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0086"
  - "murF"
---

# murF

`gene.b0086`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0086`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murF (gene.b0086) is a gene entity. It encodes murF (protein.P11880). Encoded protein function: FUNCTION: Involved in cell wall formation. Catalyzes the final step in the synthesis of UDP-N-acetylmuramoyl-pentapeptide, the precursor of murein. {ECO:0000255|HAMAP-Rule:MF_02019, ECO:0000269|PubMed:2186811}. EcoCyc product frame: UDP-NACMURALGLDAPAALIG-MONOMER. EcoCyc synonyms: mra. Genomic coordinates: 94650-96008. EcoCyc protein note: UDP-N-acetylmuramoylalanyl-D-glutamyl-2,6-diaminopimelate-D-alanyl-D-alanine ligase (MurF) catalyzes the final cytoplasmic step in the biosynthesis of the peptidoglycan precursor . Data from kinetic characterization of the enzyme is consistent with a sequential ordered reaction mechanism, with sequential binding of ATP, tripeptide, and D-Ala-D-Ala . Carbamylation of the Lys202 residue is important for catalytic activity . A crystal structure of the apo-enzyme has been solved at 2.3Å resolution . A temperature-sensitive murF mutant has been isolated . The murF2 allele was determined to carry an A288T mutation in a conserved region of the enzyme; the mutant is 181-fold less catalytically active at the permissive temperature, with even lower activity at the nonpermissive temperature. Additional site-directed mutants in the conserved E158 and H188 residues have strongly reduced catalytic activity...

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11880|protein.P11880]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=murF; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=murF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000313,ECOCYC:EG10622,GeneID:944813`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:94650-96008:+; feature_type=gene
