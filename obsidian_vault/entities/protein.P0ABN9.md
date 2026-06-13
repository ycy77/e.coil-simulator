---
entity_id: "protein.P0ABN9"
entity_type: "protein"
name: "dcuB"
source_database: "UniProt"
source_id: "P0ABN9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:21634397}; Multi-pass membrane protein {ECO:0000269|PubMed:21634397}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dcuB genF b4123 JW4084"
---

# dcuB

`protein.P0ABN9`

## Static

- Type: `protein`
- Source: `UniProt:P0ABN9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:21634397}; Multi-pass membrane protein {ECO:0000269|PubMed:21634397}.

## Enriched Summary

FUNCTION: Bifunctional protein with a transport and a regulatory function (PubMed:18957436, PubMed:27318186). Responsible for the transport of C4-dicarboxylates during anaerobic growth (PubMed:17643228, PubMed:7961398, PubMed:8131924, PubMed:8955408). Catalyzes the uptake of fumarate, malate, aspartate or D-tartrate coupled to the export of succinate (PubMed:17643228, PubMed:7961398, PubMed:8955408). Can also catalyze the uptake (without exchange) of fumarate (PubMed:8955408). May function primarily as a C4-dicarboxylate transporter during fumarate respiration (PubMed:9852003). Required for anaerobic growth on D-tartrate (PubMed:17643228). {ECO:0000269|PubMed:17643228, ECO:0000269|PubMed:18957436, ECO:0000269|PubMed:27318186, ECO:0000269|PubMed:7961398, ECO:0000269|PubMed:8131924, ECO:0000269|PubMed:8955408, ECO:0000269|PubMed:9852003}.; FUNCTION: In addition, possesses a regulatory function, which is independent from the transport function, and is required for the response of the DcuS/DcuR two-component system to C4-dicarboxylates (PubMed:18957436, PubMed:27318186). DcuB interacts physically with DcuS and converts DcuS to the C4-dicarboxylate responsive form (PubMed:27318186). However, the site for C4-dicarboxylate perception and specificity in sensing by DcuB/DcuS is located on DcuS and not on DcuB (PubMed:27318186). {ECO:0000269|PubMed:18957436, ECO:0000269|PubMed:27318186}...

## Biological Role

Catalyzes fumarate:succinate antiport (reaction.ecocyc.TRANS-RXN-106), aspartate:succinate antiport (reaction.ecocyc.TRANS-RXN-106A), malate:succinate antiport (reaction.ecocyc.TRANS-RXN-106B), fumarate:proton symport (reaction.ecocyc.TRANS-RXN-299), succinate:tartrate antiport (reaction.ecocyc.TRANS-RXN0-499). Transports Succinate (molecule.C00042), D-tartrate (molecule.ecocyc.D-TARTRATE). Component of DcuS-DcuB sensor complex (complex.ecocyc.CPLX0-8304).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Bifunctional protein with a transport and a regulatory function (PubMed:18957436, PubMed:27318186). Responsible for the transport of C4-dicarboxylates during anaerobic growth (PubMed:17643228, PubMed:7961398, PubMed:8131924, PubMed:8955408). Catalyzes the uptake of fumarate, malate, aspartate or D-tartrate coupled to the export of succinate (PubMed:17643228, PubMed:7961398, PubMed:8955408). Can also catalyze the uptake (without exchange) of fumarate (PubMed:8955408). May function primarily as a C4-dicarboxylate transporter during fumarate respiration (PubMed:9852003). Required for anaerobic growth on D-tartrate (PubMed:17643228). {ECO:0000269|PubMed:17643228, ECO:0000269|PubMed:18957436, ECO:0000269|PubMed:27318186, ECO:0000269|PubMed:7961398, ECO:0000269|PubMed:8131924, ECO:0000269|PubMed:8955408, ECO:0000269|PubMed:9852003}.; FUNCTION: In addition, possesses a regulatory function, which is independent from the transport function, and is required for the response of the DcuS/DcuR two-component system to C4-dicarboxylates (PubMed:18957436, PubMed:27318186). DcuB interacts physically with DcuS and converts DcuS to the C4-dicarboxylate responsive form (PubMed:27318186). However, the site for C4-dicarboxylate perception and specificity in sensing by DcuB/DcuS is located on DcuS and not on DcuB (PubMed:27318186). {ECO:0000269|PubMed:18957436, ECO:0000269|PubMed:27318186}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-106|reaction.ecocyc.TRANS-RXN-106]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-106A|reaction.ecocyc.TRANS-RXN-106A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-106B|reaction.ecocyc.TRANS-RXN-106B]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-299|reaction.ecocyc.TRANS-RXN-299]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-499|reaction.ecocyc.TRANS-RXN0-499]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8304|complex.ecocyc.CPLX0-8304]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `transports` --> [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.D-TARTRATE|molecule.ecocyc.D-TARTRATE]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4123|gene.b4123]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABN9`
- `KEGG:ecj:JW4084;eco:b4123;ecoc:C3026_22280;`
- `GeneID:93777709;948641;`
- `GO:GO:0005469; GO:0005886; GO:0009061; GO:0015293; GO:0015556; GO:0015740`

## Notes

Anaerobic C4-dicarboxylate transporter DcuB
