---
entity_id: "gene.b0142"
entity_type: "gene"
name: "folK"
source_database: "NCBI RefSeq"
source_id: "gene-b0142"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0142"
  - "folK"
---

# folK

`gene.b0142`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0142`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

folK (gene.b0142) is a gene entity. It encodes folK (protein.P26281). Encoded protein function: FUNCTION: Catalyzes the transfer of pyrophosphate from adenosine triphosphate (ATP) to 6-hydroxymethyl-7,8-dihydropterin, an enzymatic step in folate biosynthesis pathway. {ECO:0000269|PubMed:1325970}. EcoCyc product frame: H2PTERIDINEPYROPHOSPHOKIN-MONOMER. Genomic coordinates: 157253-157732. EcoCyc protein note: 6-hydroxymethyl-7,8-dihydropterin pyrophosphokinase (HPPK) catalyzes a reaction in the folate biosynthesis pathway, the transfer of pyrophosphate from ATP to 6-hydroxymethyl-7,8-dihydropterin . HPPK is essential in microorganisms, and the enzyme is not present in mammals; it is therefore a target for the development of antimicrobial drugs. Various crystal and solution structures of HPPK have been solved and have elucidated the reaction mechanism and kinetics. The protein undergoes conformational changes during the catalytic cycle. The enzyme binds ATP first, which then enables faster binding of 6-hydroxymethyl-7,8-dihydropterin (HMDP) . Mg2+ is important for binding of both ATP and HMDP . The roles in substrate binding and catalysis of several amino acid residues in the flexible loop 3 have been investigated by site-directed mutagenesis . Substrate site inhibitors have been synthesized and tested...

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26281|protein.P26281]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=folK; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=folK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000491,ECOCYC:EG11374,GeneID:948792`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:157253-157732:-; feature_type=gene
