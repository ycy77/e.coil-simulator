---
entity_id: "gene.b4171"
entity_type: "gene"
name: "miaA"
source_database: "NCBI RefSeq"
source_id: "gene-b4171"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4171"
  - "miaA"
---

# miaA

`gene.b4171`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4171`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

miaA (gene.b4171) is a gene entity. It encodes miaA (protein.P16384). Encoded protein function: FUNCTION: Catalyzes the transfer of a dimethylallyl group onto the adenine at position 37 in tRNAs that read codons beginning with uridine, leading to the formation of N6-(dimethylallyl)adenosine (i(6)A). {ECO:0000269|PubMed:9012675, ECO:0000269|PubMed:9148919}. EcoCyc product frame: EG10595-MONOMER. EcoCyc synonyms: trpX. Genomic coordinates: 4399252-4400202. EcoCyc protein note: Dimethylallyl diphosphate:tRNA dimethylallyltransferase (DMAPP-tRNA transferase, MiaA) catalyzes the first step in the pathway for hypermodification of the A37 base of certain tRNAs such as tRNATyr and tRNAPhe. Further thiomethylation of the A37 position is dependent on the presence of the isopentenyl modification . MiaA transfers the dimethylallyl moiety of DMAPP to the N6 position of A37, which is adjacent to the anticodon . This modification is required for efficient binding of tRNATyr to ribosomes and is important in preventing frameshifts and other mutations . MiaA-catalyzed tRNA modification is involved in regulating the translation efficiency of modification-tunable transcripts (MoTTs) . MiaA can act on isolated tRNA stem-loops, as long as the helix stem and the A36-A37-A38 motif are both present...

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16384|protein.P16384]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=miaA; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=miaA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013657,ECOCYC:EG10595,GeneID:948690`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4399252-4400202:+; feature_type=gene
