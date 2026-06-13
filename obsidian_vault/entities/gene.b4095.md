---
entity_id: "gene.b4095"
entity_type: "gene"
name: "phnM"
source_database: "NCBI RefSeq"
source_id: "gene-b4095"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4095"
  - "phnM"
---

# phnM

`gene.b4095`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4095`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnM (gene.b4095) is a gene entity. It encodes phnM (protein.P16689). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of alpha-D-ribose 1-methylphosphonate triphosphate (RPnTP) to form alpha-D-ribose 1-methylphosphonate phosphate (PRPn) and diphosphate. {ECO:0000269|PubMed:22089136}. EcoCyc product frame: EG10722-MONOMER. Genomic coordinates: 4316082-4317218. EcoCyc protein note: PhnM catalyzes hydrolysis of CPD0-2479, generating CPD0-2480 and pyrophosphate . PhnM is a member of the amidohydrolase superfamily . phnM is part of an operon that is phosphate starvation-inducible and required for use of phosphonate and phosphite as phosphorous sources . PhnM appeared to be required for carbon-phosphorous lyase activity .

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16689|protein.P16689]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnM; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013419,ECOCYC:EG10722,GeneID:948613`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4316082-4317218:-; feature_type=gene
