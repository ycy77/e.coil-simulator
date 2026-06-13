---
entity_id: "gene.b1819"
entity_type: "gene"
name: "manZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1819"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1819"
  - "manZ"
---

# manZ

`gene.b1819`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1819`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

manZ (gene.b1819) is a gene entity. It encodes manZ (protein.P69805). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ManXYZ PTS system is involved in mannose transport. {ECO:0000269|PubMed:2951378, ECO:0000269|PubMed:2999119}.; FUNCTION: Also functions as a receptor for bacterial chemotaxis and is required for infection of the cell by bacteriophage lambda where it most likely functions as a pore for penetration of lambda DNA. {ECO:0000269|PubMed:353494, ECO:0000269|PubMed:4604906}. EcoCyc product frame: MANZ-MONOMER. EcoCyc synonyms: gptB, mpt, ptsM, ptsX. Genomic coordinates: 1903895-1904746. EcoCyc protein note: ManZ is a moderately hydrophobic membrane protein which together with ManY forms the transmembrane channel of the E. coli ManXYZ mannose permease . ManZ contains a PTS Enzyme IID domain. The ManZ and ManY proteins alone are sufficient for penetration of λ phage DNA...

## Biological Role

Repressed by sgrS (gene.b4577), nagC (protein.P0AF20). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69805|protein.P69805]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=manZ; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=manZ; function=+
- `represses` <-- [[gene.b4577|gene.b4577]] `RegulonDB` `S` - regulator=SgrS; target=manZ; function=-
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `S` - regulator=NagC; target=manZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006058,ECOCYC:EG10569,GeneID:946342`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1903895-1904746:+; feature_type=gene
