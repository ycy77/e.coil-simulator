---
entity_id: "gene.b3621"
entity_type: "gene"
name: "waaC"
source_database: "NCBI RefSeq"
source_id: "gene-b3621"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3621"
  - "waaC"
---

# waaC

`gene.b3621`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3621`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

waaC (gene.b3621) is a gene entity. It encodes waaC (protein.P24173). Encoded protein function: FUNCTION: Glycosyltransferase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS) (PubMed:11054112, PubMed:9446588). Catalyzes the addition of the first heptose unit to one 3-deoxy-D-manno-octulosonic acid (Kdo) residue of the Kdo2-lipid A module (PubMed:11054112, PubMed:11717579, PubMed:9446588). The analog ADP-mannose can serve as an alternative donor in place of ADP-L-glycero-D-manno-heptose for the glycosylation of Kdo2-lipid A (PubMed:9446588). Displays no activity with ADP-glucose, GDP-mannose, UDP-glucose or UDP-galactose (PubMed:9446588). {ECO:0000269|PubMed:11054112, ECO:0000269|PubMed:11717579, ECO:0000269|PubMed:9446588}. EcoCyc product frame: EG11189-MONOMER. EcoCyc synonyms: rfa-2, rfaC, yibC. Genomic coordinates: 3795979-3796938. EcoCyc protein note: ADP-heptose:LPS heptosyltransferase I (HepI) is the enzyme responsible for transfer of the first heptose sugar onto the Kdo2 moiety of the lipopolysaccharide inner core . HepI is able to catalyze heptose transfer to underacylated and fully deacylated Kdo2-lipid A analogs; this activity does not require addition of detergent. Thus, the enzyme appears to only recognize the Kdo sugar region of these acceptor molecules...

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24173|protein.P24173]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=waaC; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=waaC; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=waaC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011847,ECOCYC:EG11189,GeneID:948136`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3795979-3796938:+; feature_type=gene
