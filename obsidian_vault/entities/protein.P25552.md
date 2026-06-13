---
entity_id: "protein.P25552"
entity_type: "protein"
name: "gppA"
source_database: "UniProt"
source_id: "P25552"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gppA gpp b3779 JW5603"
---

# gppA

`protein.P25552`

## Static

- Type: `protein`
- Source: `UniProt:P25552`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of pppGpp to ppGpp. Guanosine pentaphosphate (pppGpp) is a cytoplasmic signaling molecule which together with ppGpp controls the 'stringent response', an adaptive process that allows bacteria to respond to amino acid starvation, resulting in the coordinated regulation of numerous cellular activities (PubMed:6130093, PubMed:8394006). In vitro, can hydrolyze pppGp (PubMed:6130093). Also has exopolyphosphatase activity, catalyzing the release of orthophosphate by processive hydrolysis of the phosphoanyhydride bonds of polyphosphate chains (1000 residues) (PubMed:8394006). {ECO:0000269|PubMed:6130093, ECO:0000269|PubMed:8394006}.

## Biological Role

Catalyzes guanosine 3'-diphosphate 5'-triphosphate 5'-phosphohydrolase (reaction.R03409). Component of guanosine-5'-triphosphate,3'-diphosphate phosphatase (complex.ecocyc.PPPGPPHYDRO-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of pppGpp to ppGpp. Guanosine pentaphosphate (pppGpp) is a cytoplasmic signaling molecule which together with ppGpp controls the 'stringent response', an adaptive process that allows bacteria to respond to amino acid starvation, resulting in the coordinated regulation of numerous cellular activities (PubMed:6130093, PubMed:8394006). In vitro, can hydrolyze pppGp (PubMed:6130093). Also has exopolyphosphatase activity, catalyzing the release of orthophosphate by processive hydrolysis of the phosphoanyhydride bonds of polyphosphate chains (1000 residues) (PubMed:8394006). {ECO:0000269|PubMed:6130093, ECO:0000269|PubMed:8394006}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03409|reaction.R03409]] `KEGG` `database` - via EC:3.6.1.11
- `is_component_of` --> [[complex.ecocyc.PPPGPPHYDRO-CPLX|complex.ecocyc.PPPGPPHYDRO-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3779|gene.b3779]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25552`
- `KEGG:ecj:JW5603;eco:b3779;ecoc:C3026_20460;`
- `GeneID:75174011;948291;`
- `GO:GO:0006793; GO:0008894; GO:0015949; GO:0015970; GO:0015974; GO:0042594`
- `EC:3.6.1.40`

## Notes

Guanosine-5'-triphosphate,3'-diphosphate pyrophosphatase (EC 3.6.1.40) (Guanosine pentaphosphate phosphohydrolase) (pppGpp-5'-phosphohydrolase)
