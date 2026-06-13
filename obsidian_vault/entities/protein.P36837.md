---
entity_id: "protein.P36837"
entity_type: "protein"
name: "dtpB"
source_database: "UniProt"
source_id: "P36837"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dtpB yhiP b3496 JW3463"
---

# dtpB

`protein.P36837`

## Static

- Type: `protein`
- Source: `UniProt:P36837`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Proton-dependent permease that transports di- and tripeptides. Has a clear preference for dipeptides and tripeptides composed of L-amino acids, and discriminates dipeptides on the basis of the position of charges within the substrate. {ECO:0000269|PubMed:18485005}. The DtpB protein is a member of the POT (proton-dependent oligopeptide transporter) family of peptide transporters . DtpB is responsible for proton-dependent transport of di- and tripeptides as well as some structurally related peptidomimetics like B-lactam antibiotics . DtpB transports the tetrapeptide, tetraalanine in vitro however tetraalanine does not function as an inhibitor in competitive transport assays . DtpB shows a preference for di- and tripeptides composed of L amino acids and for peptides containing a positively charged side chain in the N-terminal position . YhiP is predicted to contain 14 transmembrane regions with the C-terminus located in the cytoplasm . The dipeptide/tripeptide:proton symporters DtpB and B1634-MONOMER DtpA are receptors for the group 6 contact-dependent growth inhibition (CDI) ionophore toxins . dtpB: dipeptide and tripeptide permease B

## Biological Role

Catalyzes tripeptide:proton symport (reaction.ecocyc.TRANS-RXN0-267), dipeptide:proton symport (reaction.ecocyc.TRANS-RXN0-288).

## Annotation

FUNCTION: Proton-dependent permease that transports di- and tripeptides. Has a clear preference for dipeptides and tripeptides composed of L-amino acids, and discriminates dipeptides on the basis of the position of charges within the substrate. {ECO:0000269|PubMed:18485005}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-267|reaction.ecocyc.TRANS-RXN0-267]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-288|reaction.ecocyc.TRANS-RXN0-288]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3496|gene.b3496]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36837`
- `KEGG:ecj:JW3463;eco:b3496;ecoc:C3026_18935;`
- `GeneID:75205773;948006;`
- `GO:GO:0005886; GO:0015031; GO:0015078; GO:0015333; GO:0035442; GO:0035443; GO:0042937; GO:0071916; GO:1902600`

## Notes

Dipeptide and tripeptide permease B
