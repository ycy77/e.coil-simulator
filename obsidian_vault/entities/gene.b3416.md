---
entity_id: "gene.b3416"
entity_type: "gene"
name: "malQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3416"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3416"
  - "malQ"
---

# malQ

`gene.b3416`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3416`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malQ (gene.b3416) is a gene entity. It encodes malQ (protein.P15977). Encoded protein function: 4-alpha-glucanotransferase (EC 2.4.1.25) (Amylomaltase) (Disproportionating enzyme) (D-enzyme) EcoCyc product frame: AMYLOMALT-MONOMER. EcoCyc synonyms: malA. Genomic coordinates: 3547986-3550070. EcoCyc protein note: Amylomaltase (MalQ) was first described as a maltose-inducible enzyme that catalyzes a reversible transglycosidase reaction . The enzyme belongs to the glycoside hydrolase family GH77 of 4-α-glucanotransferases that catalyzes transglycosylation of maltose and maltodextrins. MalQ does not have maltase activity, i.e. it does not hydrolyze maltose to form two molecules of glucose . The specificity of MalQ for donor and acceptor molecules of the transglycosylation reaction has been difficult to ascertain. It was initially reported that maltose serves as an acceptor substrate of the enzyme . Further experiments using more highly purified maltose suggested that maltose is a poor acceptor . Later, it was demonstrated that the enzyme can utilize purified 14C-maltose to produce labeled maltodextrins and glucose . Maltotetraose appears to be the most efficient substrate . Kinetic data of the utilization of maltose and higher oligomers alone or with the addition of glucose have been measured...

## Biological Role

Activated by malT (protein.P06993), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15977|protein.P15977]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P06993|protein.P06993]] `RegulonDB` `C` - regulator=MalT; target=malQ; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=malQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011151,ECOCYC:EG10561,GeneID:947923`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3547986-3550070:-; feature_type=gene
