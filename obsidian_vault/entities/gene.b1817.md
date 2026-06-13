---
entity_id: "gene.b1817"
entity_type: "gene"
name: "manX"
source_database: "NCBI RefSeq"
source_id: "gene-b1817"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1817"
  - "manX"
---

# manX

`gene.b1817`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1817`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

manX (gene.b1817) is a gene entity. It encodes manX (protein.P69797). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II ManXYZ PTS system is involved in mannose transport. {ECO:0000269|PubMed:2681202, ECO:0000269|PubMed:2951378, ECO:0000269|PubMed:2999119, ECO:0000269|PubMed:8262947}.; FUNCTION: Also functions as a receptor for bacterial chemotaxis and is required for infection of the cell by bacteriophage lambda where it most likely functions as a pore for penetration of lambda DNA. {ECO:0000269|PubMed:353494, ECO:0000269|PubMed:4604906}. EcoCyc product frame: MANX-MONOMER. EcoCyc synonyms: gptB, mpt, ptsL, ptsX. Genomic coordinates: 1902048-1903019. EcoCyc protein note: The ManX subunit of the mannose PTS permease consists of two domains, IIAman and IIBman, linked by a hinge peptide. Each domain contains a phosphorylation site and phosphoryl transfer occurs between His-10 of IIA and His-175 of IIB . ManX exists as a dimer and is found membrane associated as well as free in the cytoplasm...

## Biological Role

Repressed by dicF (gene.b1574), sgrS (gene.b4577), hfq (protein.P0A6X3), nagC (protein.P0AF20). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69797|protein.P69797]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=manX; function=+
- `represses` <-- [[gene.b1574|gene.b1574]] `RegulonDB` `S` - regulator=DicF; target=manX; function=-
- `represses` <-- [[gene.b4577|gene.b4577]] `RegulonDB` `S` - regulator=SgrS; target=manX; function=-
- `represses` <-- [[protein.P0A6X3|protein.P0A6X3]] `RegulonDB|EcoCyc` `C` - regulator=Hfq; target=manX; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `S` - regulator=NagC; target=manX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006054,ECOCYC:EG10567,GeneID:946334`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1902048-1903019:+; feature_type=gene
