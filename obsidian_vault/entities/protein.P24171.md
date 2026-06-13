---
entity_id: "protein.P24171"
entity_type: "protein"
name: "dcp"
source_database: "UniProt"
source_id: "P24171"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:8226676}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dcp b1538 JW1531"
---

# dcp

`protein.P24171`

## Static

- Type: `protein`
- Source: `UniProt:P24171`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:8226676}.

## Enriched Summary

FUNCTION: Removes dipeptides from the C-termini of N-blocked tripeptides, tetrapeptides and larger peptides. {ECO:0000269|PubMed:8226676}. Dipeptidyl carboxypeptidase is a peptidase capable of cleaving peptide bonds in amino-blocked small peptide substrates . It is required for growth when only amino-blocked peptides such as N-acetyl-alanylalanylalanine and N-benzoyl-glycylhistidylleucine are available as carbon sources . A fraction of the total pool of dipeptidyl carboxypeptidase is in the periplasm . Dcp- mutants are unable to grow with N-acetylalanylalanylalanine as the sole nitrogen source . Recombinant enzyme purified from cell extracts appeared to be a monomer based on an apparent molecular mass of 80 kDa by gel filtration chromatography and 78 kDa by SDS-PAGE . Protease inhibitors and divalent cations had varying effects on enzymatic activity. PMSF showed little inhibition; the cysteine protease inhibitor E64, trypsin inhibitors, pepstatin, EDTA, and NaCl showed some inhibition; chymostatin was a relatively stronger inhibitor; and 1,10-phenanthroline completely inhibited. Among divalent cations, some activation was seen with Mn2+, Mg2+, Ca2+ and Co2+. Strong inhibitors included Cu2+, Zn2+ and Ni2+ . In contrast, a His6-tagged recombinant enzyme had somewhat different properties including activation rather than inhibition by Zn2+ and NaCl...

## Biological Role

Catalyzes 3.4.15.5-RXN (reaction.ecocyc.3.4.15.5-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

FUNCTION: Removes dipeptides from the C-termini of N-blocked tripeptides, tetrapeptides and larger peptides. {ECO:0000269|PubMed:8226676}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.15.5-RXN|reaction.ecocyc.3.4.15.5-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1538|gene.b1538]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24171`
- `KEGG:ecj:JW1531;eco:b1538;ecoc:C3026_08885;`
- `GeneID:946084;`
- `GO:GO:0004180; GO:0004222; GO:0005737; GO:0005829; GO:0006508; GO:0008241; GO:0030288; GO:0046872`
- `EC:3.4.15.5`

## Notes

Dipeptidyl carboxypeptidase (EC 3.4.15.5) (Peptidyl-dipeptidase Dcp)
