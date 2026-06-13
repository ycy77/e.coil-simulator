---
entity_id: "molecule.C00018"
entity_type: "small_molecule"
name: "Pyridoxal phosphate"
source_database: "KEGG"
source_id: "C00018"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pyridoxal phosphate"
  - "Pyridoxal 5'-phosphate"
  - "Pyridoxal 5-phosphate"
  - "PLP"
---

# Pyridoxal phosphate

`molecule.C00018`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00018`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pyridoxal phosphate; Pyridoxal 5'-phosphate; Pyridoxal 5-phosphate; PLP EcoCyc common name: pyridoxal 5'-phosphate. PYRIDOXAL_PHOSPHATE "Pyridoxal 5'-phosphate" (PLP, vitamin B6) is an essential cofactor in all living systems . It is one of the most versatile cofactors and participates in transamination, decarboxylation, racemization, Cα-Cβ cleavage and α-β elimination reactions. PLP plays an important role in amino acid and carbohydrate metabolism and has been implicated in singlet oxygen resistance . In most enzymes the aldehyde group of PLP forms a Schiff-base linkage (internal aldimine) with the ε-amino group of a specific lysine residue at the active site. An amino group of the substrate displaces the ε-amino group of the active-site lysine residue in a process known as transaldimination. The resulting external aldimine can lose a proton, carbon dioxide, or an amino acid sidechain to become a quinonoid intermediate, which in turn can act as a nucleophile in several reaction pathways. It should be noted that while this is the most common mechanisms, exceptions do occur - for example, EC-2.4.1.1, which utilizes the phosphate group on PLP to perform its reaction, and EC-4.2.1.168, which has a histidine instead of a lysine in the active site and converts PLP to the PYRIDOXAMINE-5P (PMP) form...

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 7 reaction(s). Binds 8-amino-7-oxononanoate synthase (complex.ecocyc.7KAPSYN-CPLX), N-acetylornithine aminotransferase / N-succinyldiaminopimelate aminotransferase (complex.ecocyc.ACETYLORNTRANSAM-CPLX), cysteine synthase A (complex.ecocyc.ACSERLYA-CPLX), cysteine synthase B (complex.ecocyc.ACSERLYB-CPLX), aminodeoxychorismate lyase (complex.ecocyc.ADCLY-CPLX), 2-amino-3-ketobutyrate CoA ligase (complex.ecocyc.AKBLIG-CPLX), biosynthetic arginine decarboxylase (complex.ecocyc.ARGDECARBOXBIO-CPLX), arginine decarboxylase, degradative (complex.ecocyc.ARGDECARBOXDEG-CPLX), and 45 more.

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)

## Annotation

KEGG compound: Pyridoxal phosphate; Pyridoxal 5'-phosphate; Pyridoxal 5-phosphate; PLP

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00750` Vitamin B6 metabolism (KEGG)

## Outgoing Edges (72)

- `activates` --> [[reaction.ecocyc.GLUC1PADENYLTRANS-RXN|reaction.ecocyc.GLUC1PADENYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `binds` --> [[complex.ecocyc.7KAPSYN-CPLX|complex.ecocyc.7KAPSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ACETYLORNTRANSAM-CPLX|complex.ecocyc.ACETYLORNTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ACSERLYA-CPLX|complex.ecocyc.ACSERLYA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ACSERLYB-CPLX|complex.ecocyc.ACSERLYB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ADCLY-CPLX|complex.ecocyc.ADCLY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.AKBLIG-CPLX|complex.ecocyc.AKBLIG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ARGDECARBOXBIO-CPLX|complex.ecocyc.ARGDECARBOXBIO-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ARGDECARBOXDEG-CPLX|complex.ecocyc.ARGDECARBOXDEG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ASPAMINOTRANS-DIMER|complex.ecocyc.ASPAMINOTRANS-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX|complex.ecocyc.BRANCHED-CHAINAMINOTRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-1141|complex.ecocyc.CPLX0-1141]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-1401|complex.ecocyc.CPLX0-1401]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-2401|complex.ecocyc.CPLX0-2401]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-246|complex.ecocyc.CPLX0-246]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-248|complex.ecocyc.CPLX0-248]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7465|complex.ecocyc.CPLX0-7465]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7838|complex.ecocyc.CPLX0-7838]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7990|complex.ecocyc.CPLX0-7990]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8092|complex.ecocyc.CPLX0-8092]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8159|complex.ecocyc.CPLX0-8159]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8202|complex.ecocyc.CPLX0-8202]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8561|complex.ecocyc.CPLX0-8561]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX|complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.DAPASYN-CPLX|complex.ecocyc.DAPASYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.DCYSDESULF-CPLX|complex.ecocyc.DCYSDESULF-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.DIAMINOPIMDECARB-CPLX|complex.ecocyc.DIAMINOPIMDECARB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GABATRANSAM-CPLX|complex.ecocyc.GABATRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GCVP-CPLX|complex.ecocyc.GCVP-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GLUTDECARBOXA-CPLX|complex.ecocyc.GLUTDECARBOXA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GLUTDECARBOXB-CPLX|complex.ecocyc.GLUTDECARBOXB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GLYCOPHOSPHORYL-CPLX|complex.ecocyc.GLYCOPHOSPHORYL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GLYOHMETRANS-CPLX|complex.ecocyc.GLYOHMETRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GSAAMINOTRANS-CPLX|complex.ecocyc.GSAAMINOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.LDC2-CPLX|complex.ecocyc.LDC2-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.LTAA-CPLX|complex.ecocyc.LTAA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.LYSDECARBOX-CPLX|complex.ecocyc.LYSDECARBOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.MALDEXPHOSPHORYL-CPLX|complex.ecocyc.MALDEXPHOSPHORYL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX|complex.ecocyc.O-SUCCHOMOSERLYASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ORNDECARBOX-BIO-CPLX|complex.ecocyc.ORNDECARBOX-BIO-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.ORNDECARBOXDEG-CPLX|complex.ecocyc.ORNDECARBOXDEG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.PSERTRANSAM-CPLX|complex.ecocyc.PSERTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.SUCCORNTRANSAM-CPLX|complex.ecocyc.SUCCORNTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.THREDEHYDCAT-CPLX|complex.ecocyc.THREDEHYDCAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.THREDEHYDSYN-CPLX|complex.ecocyc.THREDEHYDSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.TRYPSYN|complex.ecocyc.TRYPSYN]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.TRYPTOPHAN-CPLX|complex.ecocyc.TRYPTOPHAN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.TYRB-DIMER|complex.ecocyc.TYRB-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P00926|protein.P00926]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P00934|protein.P00934]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P09053|protein.P09053]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P39280|protein.P39280]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P50457|protein.P50457]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P77690|protein.P77690]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.R00174|reaction.R00174]] `KEGG` `database` - C00002 + C00250 <=> C00008 + C00018
- `is_product_of` --> [[reaction.R00277|reaction.R00277]] `KEGG` `database` - C00647 + C00001 + C00007 <=> C00018 + C00014 + C00027
- `is_product_of` --> [[reaction.R00278|reaction.R00278]] `KEGG` `database` - C00627 + C00007 <=> C00027 + C00018
- `is_product_of` --> [[reaction.ecocyc.PMPOXI-RXN|reaction.ecocyc.PMPOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PNPOXI-RXN|reaction.ecocyc.PNPOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PYRIDOXKIN-RXN|reaction.ecocyc.PYRIDOXKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7074|reaction.ecocyc.RXN0-7074]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00173|reaction.R00173]] `KEGG` `database` - C00018 + C00001 <=> C00250 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.3.1.3.74-RXN|reaction.ecocyc.3.1.3.74-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5240|reaction.ecocyc.RXN0-5240]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.2.5.1.19-RXN|reaction.ecocyc.2.5.1.19-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ERYTH4PDEHYDROG-RXN|reaction.ecocyc.ERYTH4PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN|reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.OHMETHYLBILANESYN-RXN|reaction.ecocyc.OHMETHYLBILANESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PMPOXI-RXN|reaction.ecocyc.PMPOXI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PNPOXI-RXN|reaction.ecocyc.PNPOXI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYRIDOXKIN-RXN|reaction.ecocyc.PYRIDOXKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PYROXALTRANSAM-RXN|reaction.ecocyc.PYROXALTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00018`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
