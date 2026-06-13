---
entity_id: "protein.P69902"
entity_type: "protein"
name: "frc"
source_database: "UniProt"
source_id: "P69902"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frc yfdW b2374 JW2371"
---

# frc

`protein.P69902`

## Static

- Type: `protein`
- Source: `UniProt:P69902`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the catabolism of oxalate and in the adapatation to low pH via the induction of the oxalate-dependent acid tolerance response (ATR). Catalyzes the transfer of the CoA moiety from formyl-CoA to oxalate. It can also use succinate as an acceptor. {ECO:0000269|PubMed:12844490, ECO:0000269|PubMed:18245280, ECO:0000269|PubMed:23335415}. YfdW (Frc) is a formyl-CoA transferase with sequence and structural similarity to Frc from Oxalobacter formigenes, a strictly anaerobic bacterium found in the mammalian gut . Unlike the O. formigenes enzyme, the E. coli enzyme shows high substrate specificity . Crystal structures of apo-YfdW and YfdW with CoA, acetyl-CoA, or both acetyl-CoA and oxalate have been solved. YfdW is a homodimer; the ring-shaped monomers are concatenated like links of a chain . The enzymatic reaction mechanism is predicted by structural similarity to related enzymes; residue D169 is predicted to catalyze the reaction . Biochemical data indicates that the kinetic mechanism is ordered bi-bi sequential . Frc is required during the adaption phase of an oxalate-induced acid tolerance response . Expression of frc is increased when the EvgAS two-component regulatory system is overexpressed .

## Biological Role

Catalyzes formyl-CoA:oxalate CoA-transferase (reaction.R07290). Component of formyl-CoA transferase (complex.ecocyc.CPLX0-1142).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in the catabolism of oxalate and in the adapatation to low pH via the induction of the oxalate-dependent acid tolerance response (ATR). Catalyzes the transfer of the CoA moiety from formyl-CoA to oxalate. It can also use succinate as an acceptor. {ECO:0000269|PubMed:12844490, ECO:0000269|PubMed:18245280, ECO:0000269|PubMed:23335415}.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R07290|reaction.R07290]] `KEGG` `database` - via EC:2.8.3.16
- `is_component_of` --> [[complex.ecocyc.CPLX0-1142|complex.ecocyc.CPLX0-1142]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2374|gene.b2374]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69902`
- `KEGG:ecj:JW2371;eco:b2374;ecoc:C3026_13200;`
- `GeneID:75172492;75202557;946842;`
- `GO:GO:0033608; GO:0033611; GO:0071468`
- `EC:2.8.3.16`

## Notes

Formyl-CoA:oxalate CoA-transferase (FCOCT) (EC 2.8.3.16) (Formyl-coenzyme A transferase) (Formyl-CoA transferase)
