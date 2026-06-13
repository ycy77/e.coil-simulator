---
entity_id: "protein.P40719"
entity_type: "protein"
name: "qseC"
source_database: "UniProt"
source_id: "P40719"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "qseC ygiY b3026 JW2994"
---

# qseC

`protein.P40719`

## Static

- Type: `protein`
- Source: `UniProt:P40719`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Member of a two-component regulatory system QseB/QseC. Activates the flagella regulon by activating transcription of FlhDC. May activate QseB by phosphorylation. {ECO:0000269|PubMed:11929534}. This is the His-246 phosphorylated form of EG12658-MONOMER "QseC" - the sensor histidine kinase of the QseBC two-component signal transduction system. QseC is the sensor kinase component of the QseB-QseC two-component system which is involved in the activation of flagella and motility genes; QseBC modulates transcription of flhDC, the master regulator for flagella and motility genes . QseC contains two predicted transmembrane helices, a dimerization domain which contains the predicted site (His-246) of autophosphorylation and an 'orthodox-type' ATP-binding kinase domain (see ). QseC is predicted to have both histidine autokinase and phosphotransferase activity; the QseBC system has been well studied in enterohemorrhagic (EHEC) and uropathogenic (UPAC) E. coli strains (see ); QseC (purified from EHEC and reconstituted into liposomes) autophosphorylates in response to an external signal (epinephrine/norepinephrine and autoinducer-3) and transfers its phosphate to QseB in vitro (and see further ). QseC of EHEC O157:H7 and E. coli K-12 MG1655 differ by eight amino acids . qseBC null mutants show hypersensitivity to several toxic cations...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Member of a two-component regulatory system QseB/QseC. Activates the flagella regulon by activating transcription of FlhDC. May activate QseB by phosphorylation. {ECO:0000269|PubMed:11929534}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3026|gene.b3026]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P40719`
- `KEGG:ecj:JW2994;eco:b3026;ecoc:C3026_16530;`
- `GeneID:947174;`
- `GO:GO:0000155; GO:0000160; GO:0005524; GO:0005886; GO:0036094; GO:2000145`
- `EC:2.7.13.3`

## Notes

Sensor protein QseC (EC 2.7.13.3)
