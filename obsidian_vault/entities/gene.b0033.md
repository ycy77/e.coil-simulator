---
entity_id: "gene.b0033"
entity_type: "gene"
name: "carB"
source_database: "NCBI RefSeq"
source_id: "gene-b0033"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0033"
  - "carB"
---

# carB

`gene.b0033`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0033`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

carB (gene.b0033) is a gene entity. It encodes carB (protein.P00968). Encoded protein function: FUNCTION: Large subunit of the glutamine-dependent carbamoyl phosphate synthetase (CPSase). CPSase catalyzes the formation of carbamoyl phosphate from the ammonia moiety of glutamine, carbonate, and phosphate donated by ATP, constituting the first step of 2 biosynthetic pathways, one leading to arginine and/or urea and the other to pyrimidine nucleotides. The large subunit (synthetase) binds the substrates ammonia (free or transferred from glutamine from the small subunit), hydrogencarbonate and ATP and carries out an ATP-coupled ligase reaction, activating hydrogencarbonate by forming carboxy phosphate which reacts with ammonia to form carbamoyl phosphate. {ECO:0000255|HAMAP-Rule:MF_01210, ECO:0000269|PubMed:2658488, ECO:0000269|PubMed:2868386, ECO:0000269|PubMed:4944634, ECO:0000269|Ref.8}. EcoCyc product frame: CARBPSYN-LARGE. EcoCyc synonyms: pyrA. Genomic coordinates: 30817-34038. EcoCyc protein note: The CarB subunit is the synthetase component of carbamoylphosphate synthetase. It binds the two required molecules of MgATP and catalyzes the two required phosphorylation events. The large subunit consists of four structural units: the carboxyphosphate synthetic component, the oligomerization domain, the carbamoyl phosphate synthetic component and the allosteric domain...

## Biological Role

Repressed by argR (protein.P0A6D0), purR (protein.P0ACP7), pepA (protein.P68767). Activated by rpoD (protein.P00579), rutR (protein.P0ACU2).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00968|protein.P00968]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=carB; function=+
- `activates` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `C` - regulator=RutR; target=carB; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=carB; function=-
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=carB; function=-
- `represses` <-- [[protein.P68767|protein.P68767]] `RegulonDB` `S` - regulator=PepA; target=carB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000121,ECOCYC:EG10135,GeneID:944775`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:30817-34038:+; feature_type=gene
