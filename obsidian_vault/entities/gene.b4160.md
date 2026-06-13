---
entity_id: "gene.b4160"
entity_type: "gene"
name: "psd"
source_database: "NCBI RefSeq"
source_id: "gene-b4160"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4160"
  - "psd"
---

# psd

`gene.b4160`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4160`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

psd (gene.b4160) is a gene entity. It encodes psd (protein.P0A8K1). Encoded protein function: FUNCTION: Catalyzes the formation of phosphatidylethanolamine (PtdEtn) from phosphatidylserine (PtdSer). Only decarboxylates the lipid-linked form of the serine moiety, and not serine alone or derivatives like phosphoserine or glycerophosphoserine. {ECO:0000255|HAMAP-Rule:MF_00662, ECO:0000269|PubMed:4598120}. EcoCyc product frame: PSD-MONOMER. Genomic coordinates: 4389392-4390360. EcoCyc protein note: This subunit contains the pyruvate prosthetic group . EcoCyc protein note: Phosphatidylserine decarboxylase catalyzes the formation of phosphatidylethanolamine, the most abundant phospholipid in E. coli membranes. Phosphatidylserine decarboxylase is one of a small class of enzymes that use a covalently bound pyruvoyl prosthetic group. The pyruvoyl group is thought to act analogously to pyridoxal phosphate cofactor by forming a Schiff base between its carbonyl residue and the amino group of the substrate and then serving as an electron sink to facilitate the decarboxylation. The pyruvoyl group is essential for catalytic activity and can be inactivated by carbonyl reagents . E. coli encodes two more members of this class of enzymes, CPLX0-2901 and SAMDECARB-CPLX...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8K1|protein.P0A8K1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=psd; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013623,ECOCYC:EG10775,GeneID:948673`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4389392-4390360:-; feature_type=gene
