---
entity_id: "protein.P63235"
entity_type: "protein"
name: "gadC"
source_database: "UniProt"
source_id: "P63235"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22407317}; Multi-pass membrane protein {ECO:0000269|PubMed:22407317}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gadC acsA xasA b1492 JW1487"
---

# gadC

`protein.P63235`

## Static

- Type: `protein`
- Source: `UniProt:P63235`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22407317}; Multi-pass membrane protein {ECO:0000269|PubMed:22407317}.

## Enriched Summary

FUNCTION: Involved in glutaminase-dependent acid resistance (PubMed:30498489, PubMed:8682809). Exchanges extracellular glutamate (Glu) for intracellular gamma-aminobutyric acid (GABA) under acidic conditions (PubMed:22407317, PubMed:23589309). The protonation states of substrates are crucial for transport. Selectively transports Glu with no net charge and GABA with a positive charge (PubMed:23589309). Also efficiently transports glutamine and, to a smaller extent, methionine and leucine (PubMed:22407317). When the extracellular pH drops below 2.5, can import L-glutamine and export either glutamate or GABA (PubMed:30498489). The ability to survive the extremely acidic conditions of the stomach is essential for successful colonization of the host by commensal and pathogenic bacteria (PubMed:30498489, PubMed:8682809). {ECO:0000269|PubMed:22407317, ECO:0000269|PubMed:23589309, ECO:0000269|PubMed:30498489, ECO:0000269|PubMed:8682809, ECO:0000305|PubMed:30498489, ECO:0000305|PubMed:8682809}. GadC, a glutamic acid:γ-aminobutyrate antiporter, is part of the glutamate-dependent acid resistance system 2 (AR2) which confers resistance to extreme acid conditions. When cells are grown at pH 2.5 with glutamate, the internal pH reaches 4.2 which reflects the pH optimum of the glutamate decarboxylases...

## Biological Role

Catalyzes L-glutamine:4-aminobutanoate antiport (reaction.ecocyc.TRANS-RXN-1549), L-glutamate:4-aminobutanoate antiport (reaction.ecocyc.TRANS-RXN-261). Transports L-Glutamine (molecule.C00064), 4-Aminobutanoate (molecule.C00334).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Involved in glutaminase-dependent acid resistance (PubMed:30498489, PubMed:8682809). Exchanges extracellular glutamate (Glu) for intracellular gamma-aminobutyric acid (GABA) under acidic conditions (PubMed:22407317, PubMed:23589309). The protonation states of substrates are crucial for transport. Selectively transports Glu with no net charge and GABA with a positive charge (PubMed:23589309). Also efficiently transports glutamine and, to a smaller extent, methionine and leucine (PubMed:22407317). When the extracellular pH drops below 2.5, can import L-glutamine and export either glutamate or GABA (PubMed:30498489). The ability to survive the extremely acidic conditions of the stomach is essential for successful colonization of the host by commensal and pathogenic bacteria (PubMed:30498489, PubMed:8682809). {ECO:0000269|PubMed:22407317, ECO:0000269|PubMed:23589309, ECO:0000269|PubMed:30498489, ECO:0000269|PubMed:8682809, ECO:0000305|PubMed:30498489, ECO:0000305|PubMed:8682809}.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1549|reaction.ecocyc.TRANS-RXN-1549]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-261|reaction.ecocyc.TRANS-RXN-261]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1492|gene.b1492]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63235`
- `KEGG:ecj:JW1487;eco:b1492;ecoc:C3026_08640;`
- `GeneID:93775651;946057;`
- `GO:GO:0005886; GO:0006865; GO:0015297; GO:0022857; GO:0051454`

## Notes

Glutamate/gamma-aminobutyrate antiporter (Glu/GABA antiporter) (Extreme acid sensitivity protein)
