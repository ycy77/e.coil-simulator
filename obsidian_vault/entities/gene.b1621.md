---
entity_id: "gene.b1621"
entity_type: "gene"
name: "malX"
source_database: "NCBI RefSeq"
source_id: "gene-b1621"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1621"
  - "malX"
---

# malX

`gene.b1621`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1621`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malX (gene.b1621) is a gene entity. It encodes malX (protein.P19642). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in maltose transport. MalX can also recognize and transport glucose even though this sugar may not represent the natural substrate of the system. {ECO:0000269|PubMed:1856179}. EcoCyc product frame: MALX-MONOMER. Genomic coordinates: 1699355-1700947. EcoCyc protein note: The deduced amino acid sequence of MalX displays 35% identity with PTSG-MONOMER "PtsG" (Enzyme IIBCglc of the glucose PTS). The constitutive expression of chromosomal malX (through a malI::Tn10 mutation) restores growth on glucose in an E. coli ΔptsG ΔptsM strain provided cytoplasmic glucokinase (encoded by glk) is present. This suggests that the MalX protein can transport glucose via facilitated diffusion . Overexpression of malX from a plasmid restores growth on glucose in a ΔptsG ΔptsM Δglk strain which suggests that MalX also functions, albeit inefficiently, in vectorial phosphorylation of glucose possibly in conjunction with CRR-MONOMER "Crr" (Enzyme IIAglc) . MalX may also transport maltose by facilitated diffusion...

## Biological Role

Repressed by malI (protein.P18811). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19642|protein.P19642]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=malX; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=malX; function=+
- `represses` <-- [[protein.P18811|protein.P18811]] `RegulonDB` `S` - regulator=MalI; target=malX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005429,ECOCYC:EG10563,GeneID:946009`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1699355-1700947:+; feature_type=gene
