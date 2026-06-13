---
entity_id: "protein.P13016"
entity_type: "protein"
name: "ampD"
source_database: "UniProt"
source_id: "P13016"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:19309146}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ampD b0110 JW0106"
---

# ampD

`protein.P13016`

## Static

- Type: `protein`
- Source: `UniProt:P13016`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:19309146}.

## Enriched Summary

FUNCTION: Involved in cell wall peptidoglycan recycling (PubMed:19309146). Specifically cleaves the amide bond between the lactyl group of N-acetylmuramic acid and the alpha-amino group of the L-alanine in degradation products containing an anhydro N-acetylmuramyl moiety (PubMed:19309146). Is also involved in beta-lactamase induction (PubMed:2607970, PubMed:2691840). {ECO:0000269|PubMed:19309146, ECO:0000269|PubMed:2607970, ECO:0000269|PubMed:2691840}. AmpD is a cytosolic N-acetylmuramyl-L-alanine amidase responsible for breakdown of anhMurNAc-linked peptides, releasing the peptides for recycling . Unlike in Citrobacter freundii or Enterobacter cloacae, the native EG10040-MONOMER AmpC β-lactamase of E. coli is not inducible by β-lactam antibiotics due to lack of the AmpR regulator. In Enterobacter cloacae, the signal molecule for AmpR-dependent induction of ampC expression is anhMurNAc-pentapeptide . In an ampD mutant, 1,6-anhydro-N-acetylmuramyl-L-alanyl-D-glutamyl-meso-diaminopimelic acid (anhMurNAc-tripeptide) accumulates in the cytoplasm and, after export, in the periplasm . ampD is a member of the ampDE operon . Reviews:

## Biological Role

Catalyzes N-acetylmuramoyl-Ala amidohydrolase (reaction.R04112), RXN0-5225 (reaction.ecocyc.RXN0-5225).

## Annotation

FUNCTION: Involved in cell wall peptidoglycan recycling (PubMed:19309146). Specifically cleaves the amide bond between the lactyl group of N-acetylmuramic acid and the alpha-amino group of the L-alanine in degradation products containing an anhydro N-acetylmuramyl moiety (PubMed:19309146). Is also involved in beta-lactamase induction (PubMed:2607970, PubMed:2691840). {ECO:0000269|PubMed:19309146, ECO:0000269|PubMed:2607970, ECO:0000269|PubMed:2691840}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R04112|reaction.R04112]] `KEGG` `database` - via EC:3.5.1.28
- `catalyzes` --> [[reaction.ecocyc.RXN0-5225|reaction.ecocyc.RXN0-5225]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0110|gene.b0110]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13016`
- `KEGG:ecj:JW0106;eco:b0110;ecoc:C3026_00455;`
- `GeneID:75202075;948877;`
- `GO:GO:0005737; GO:0008745; GO:0009253; GO:0009254; GO:0009392; GO:0046872; GO:0071555`
- `EC:3.5.1.28`

## Notes

1,6-anhydro-N-acetylmuramyl-L-alanine amidase AmpD (EC 3.5.1.28) (N-acetylmuramoyl-L-alanine amidase)
