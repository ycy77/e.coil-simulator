---
entity_id: "protein.P77304"
entity_type: "protein"
name: "dtpA"
source_database: "UniProt"
source_id: "P77304"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dtpA tppB ydgR b1634 JW1626"
---

# dtpA

`protein.P77304`

## Static

- Type: `protein`
- Source: `UniProt:P77304`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Proton-dependent permease that transports di- and tripeptides as well as structurally related peptidomimetics such as aminocephalosporins into the cell. Has a clear preference for dipeptides and tripeptides composed of L-amino acids, and discriminates dipeptides on the basis of the position of charges within the substrate. {ECO:0000269|PubMed:15175316, ECO:0000269|PubMed:17158458, ECO:0000269|PubMed:18485005}. The DtpA protein (formerly TppB) is a member of the POT (proton-dependent oligopeptide transporter) family of peptide transporters also known as the PTR (peptide transport) family. DtpA is responsible for proton-dependent transport of di- and tripeptides as well as some structurally related peptidomimetics like B-lactam antibiotics . DtpA transports the tetrapeptide, tetraalanine in vitro however tetraalanine does not function as an inhibitor in competitive transport assays . DtpA shows a preference for di- and tripeptides composed of L amino acids and for peptides containing a positively charged side chain in the N-terminal position . Transmission electron microscopy of solubilised DtpA suggests a monomeric crown-like structure with a pore of approximately 8 nm . DtpA is predicted to contain 14 transmembrane regions with both termini located in the cytoplasm...

## Biological Role

Catalyzes tripeptide:proton symport (reaction.ecocyc.TRANS-RXN0-267), dipeptide:proton symport (reaction.ecocyc.TRANS-RXN0-288). Transports a dipeptide (molecule.ecocyc.DIPEPTIDES), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Proton-dependent permease that transports di- and tripeptides as well as structurally related peptidomimetics such as aminocephalosporins into the cell. Has a clear preference for dipeptides and tripeptides composed of L-amino acids, and discriminates dipeptides on the basis of the position of charges within the substrate. {ECO:0000269|PubMed:15175316, ECO:0000269|PubMed:17158458, ECO:0000269|PubMed:18485005}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-267|reaction.ecocyc.TRANS-RXN0-267]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-288|reaction.ecocyc.TRANS-RXN0-288]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.DIPEPTIDES|molecule.ecocyc.DIPEPTIDES]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1634|gene.b1634]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77304`
- `KEGG:ecj:JW1626;eco:b1634;ecoc:C3026_09390;`
- `GeneID:947436;`
- `GO:GO:0005886; GO:0015031; GO:0015333; GO:0035442; GO:0035443; GO:0042937; GO:0071916`

## Notes

Dipeptide and tripeptide permease A
