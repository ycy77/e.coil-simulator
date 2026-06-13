---
entity_id: "gene.b4005"
entity_type: "gene"
name: "purD"
source_database: "NCBI RefSeq"
source_id: "gene-b4005"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4005"
  - "purD"
---

# purD

`gene.b4005`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4005`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purD (gene.b4005) is a gene entity. It encodes purD (protein.P15640). Encoded protein function: FUNCTION: Catalyzes the reversible conversion of phosphoribosylamine to glycinamide ribonucleotide, an enzymatic step in purine biosynthesis pathway. {ECO:0000269|PubMed:2182115}. EcoCyc product frame: GLYCRIBONUCSYN-MONOMER. EcoCyc synonyms: adth(a), adth. Genomic coordinates: 4204642-4205931. EcoCyc protein note: Phosphoribosylamine—glycine ligase (glycinamide ribonucleotide synthetase, GAR synthetase) catalyzes the ligation of glycine to 5-phospho-β-D-ribosyl-amine (PRA) to produce 5-phospho-ribosyl-glycineamide (GAR) in the second step of the E. coli purine de novo biosynthesis pathway. Its kinetic mechanism for substrate binding and product release has been described as sequential and ordered. PRA was suggested to bind first, followed by ATP and glycine, with phosphate leaving first, followed by ADP and GAR. However, PRA is unstable and can hydrolyze to ribose-5-phosphate and ammonia under physiological conditions . A hypothetical docking and channeling model for the transfer of PRA from PurF to the PurD monomer has been proposed . A recombinant, poly-His-tagged Pro294Leu mutant enzyme was crystallized and its structure determined at 1.6 Å resolution . Review: Jensen, K.F., G. Dandanell, B. Hove-Jensen, and M. Willemoes (2008) "Nucleotides, Nucleosides and Nucleobases" EcoSal 3...

## Biological Role

Repressed by purR (protein.P0ACP7), rbsR (protein.P0ACQ0).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15640|protein.P15640]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=purD; function=-
- `represses` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `C` - regulator=RbsR; target=purD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013095,ECOCYC:EG10792,GeneID:948504`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4204642-4205931:-; feature_type=gene
