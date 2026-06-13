---
entity_id: "gene.b3041"
entity_type: "gene"
name: "ribB"
source_database: "NCBI RefSeq"
source_id: "gene-b3041"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3041"
  - "ribB"
---

# ribB

`gene.b3041`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3041`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ribB (gene.b3041) is a gene entity. It encodes ribB (protein.P0A7J0). Encoded protein function: FUNCTION: Catalyzes the conversion of D-ribulose 5-phosphate to formate and 3,4-dihydroxy-2-butanone 4-phosphate. {ECO:0000269|PubMed:1597419}. EcoCyc product frame: DIOHBUTANONEPSYN-MONOMER. EcoCyc synonyms: luxH, htrP, luxH-l. Genomic coordinates: 3183813-3184466. EcoCyc protein note: RibB catalyzes the synthesis of the 4-carbon compound DIHYDROXY-BUTANONE-P (3,4-dihydroxy-2-butanone 4-phosphate), a precursor of the terminal intermediate DIMETHYL-D-RIBITYL-LUMAZINE in the biosynthesis of RIBOFLAVIN . ribB is an essential gene . The enzyme is a homodimer in solution . Crystal structures have been solved at 1.55 and 1.4 Å resolution, and various amino acid residues were assigned proposed roles in catalysis and enzyme structure . A solution structure of the enzyme allowed identification of the substrate binding site, residues involved in catalysis, and identification of the Mg2+ binding site . RibB production is induced by low pH, but not by acetate and is regulated by an FMN-sensitive riboswitch that operates both on the transcriptional as well as the translational level...

## Biological Role

Repressed by FMN (molecule.C00061).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7J0|protein.P0A7J0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc regulation TYPES=Compound-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0009980,ECOCYC:EG10465,GeneID:947526`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3183813-3184466:-; feature_type=gene
