---
entity_id: "molecule.C00068"
entity_type: "small_molecule"
name: "Thiamin diphosphate"
source_database: "KEGG"
source_id: "C00068"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Thiamin diphosphate"
  - "Thiamine diphosphate"
  - "Thiamin pyrophosphate"
  - "TPP"
  - "ThPP"
---

# Thiamin diphosphate

`molecule.C00068`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00068`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Thiamin diphosphate; Thiamine diphosphate; Thiamin pyrophosphate; TPP; ThPP EcoCyc common name: thiamine diphosphate. THIAMINE Thiamin(e), also known as vitamin B1, is known to play a fundamental role in energy metabolism. Its discovery followed from the original early research on the anti-beriberi factor found in rice bran. Beriberi, a neurological disease, was particularly prevalent in Asia, where the refining of rice resulted in the removal of the thiamin-containing husk . The anti-beriberi substance was crystallized from rice polishings by Jansen and Donath in 1926 . The structure and synthesis of thiamine were reported by Williams . The compound was named thiamine when it was believed to be an amine. When it became clear that it is not an amine, it was suggested to drop the 'e' and change the name to thiamin, although both names are still in use . The active form of the vitamin in vivo is THIAMINE-PYROPHOSPHATE.

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 4 reaction(s). Binds 2-oxoglutarate dehydrogenase complex (complex.ecocyc.2OXOGLUTARATEDEH-CPLX), acetohydroxybutanoate synthase / acetolactate synthase (complex.ecocyc.ACETOLACTSYNI-CPLX), acetohydroxybutanoate synthase / acetolactate synthase (complex.ecocyc.ACETOLACTSYNII-CPLX), acetolactate synthase / acetohydroxybutanoate synthase (complex.ecocyc.ACETOLACTSYNIII-CPLX), 1-deoxy-D-xylulose-5-phosphate synthase (complex.ecocyc.CPLX0-743), 2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate synthase (complex.ecocyc.CPLX0-7525), 2-oxoglutarate decarboxylase, thiamine-requiring (complex.ecocyc.E1O), glyoxylate carboligase (complex.ecocyc.GLYOCARBOLIG-CPLX), and 5 more.

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Annotation

KEGG compound: Thiamin diphosphate; Thiamine diphosphate; Thiamin pyrophosphate; TPP; ThPP

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)

## Outgoing Edges (26)

- `binds` --> [[complex.ecocyc.2OXOGLUTARATEDEH-CPLX|complex.ecocyc.2OXOGLUTARATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ACETOLACTSYNI-CPLX|complex.ecocyc.ACETOLACTSYNI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ACETOLACTSYNII-CPLX|complex.ecocyc.ACETOLACTSYNII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ACETOLACTSYNIII-CPLX|complex.ecocyc.ACETOLACTSYNIII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-743|complex.ecocyc.CPLX0-743]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7525|complex.ecocyc.CPLX0-7525]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.E1O|complex.ecocyc.E1O]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GLYOCARBOLIG-CPLX|complex.ecocyc.GLYOCARBOLIG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.PYRUVATEDEH-CPLX|complex.ecocyc.PYRUVATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.PYRUVOXID-CPLX|complex.ecocyc.PYRUVOXID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.TRANSKETOI-CPLX|complex.ecocyc.TRANSKETOI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P52647|protein.P52647]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.ecocyc.PYRUFLAVREDUCT-MONOMER|protein.ecocyc.PYRUFLAVREDUCT-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.R00617|reaction.R00617]] `KEGG` `database` - C00002 + C01081 <=> C00008 + C00068
- `is_product_of` --> [[reaction.R04673|reaction.R04673]] `KEGG` `database` - C00109 + C05125 <=> C06006 + C00068
- `is_product_of` --> [[reaction.ecocyc.RXN-12508|reaction.ecocyc.RXN-12508]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THI-P-KIN-RXN|reaction.ecocyc.THI-P-KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00014|reaction.R00014]] `KEGG` `database` - C00022 + C00068 <=> C05125 + C00011
- `is_substrate_of` --> [[reaction.R00621|reaction.R00621]] `KEGG` `database` - C00026 + C00068 <=> C05381 + C00011
- `is_substrate_of` --> [[reaction.R04672|reaction.R04672]] `KEGG` `database` - C06010 + C00068 <=> C05125 + C00022
- `is_substrate_of` --> [[reaction.R06863|reaction.R06863]] `KEGG` `database` - C05382 + C00068 <=> C13378 + C00117
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12583|reaction.ecocyc.RXN-12583]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3542|reaction.ecocyc.RXN0-3542]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5291|reaction.ecocyc.RXN0-5291]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7041|reaction.ecocyc.RXN0-7041]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-5073|reaction.ecocyc.RXN0-5073]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00068`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
